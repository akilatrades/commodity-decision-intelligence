"""Write the SYNTHETIC physical crude book used by this project.

Every deal, ticket, invoice and swap below is invented for illustration. The
only market data is the WTI front-month proxy in data/, which sets the monthly
CMA. Four invoice errors and one short delivery are planted on purpose so the
reconciliation has something real to find; they are listed in PLANTED_BREAKS.

Run from this directory: python build_book.py
"""

from pathlib import Path

import pandas as pd

BOOK = Path("data/book")
PRICES = Path("data/cl_front_month_proxy_2026q3.csv")

# Midland and Cushing barrels are bought and moved to Houston for sale.
DEALS = [
    # id, counterparty, side, location, month, bbl, pricing, fixed, diff
    (
        "D001",
        "Permian Producer A",
        "BUY",
        "Midland",
        "2026-08",
        150_000,
        "CMA",
        None,
        0.85,
    ),
    (
        "D002",
        "Permian Producer B",
        "BUY",
        "Midland",
        "2026-08",
        90_000,
        "FIXED",
        81.90,
        None,
    ),
    (
        "D003",
        "Gulf Coast Refiner C",
        "SELL",
        "Houston",
        "2026-08",
        120_000,
        "CMA",
        None,
        1.35,
    ),
    ("D004", "Exporter D", "SELL", "Houston", "2026-08", 120_000, "CMA", None, 1.20),
    (
        "D005",
        "Permian Producer A",
        "BUY",
        "Midland",
        "2026-09",
        150_000,
        "CMA",
        None,
        0.80,
    ),
    (
        "D006",
        "Cushing Seller E",
        "BUY",
        "Cushing",
        "2026-09",
        60_000,
        "CMA",
        None,
        0.00,
    ),
    (
        "D007",
        "Gulf Coast Refiner C",
        "SELL",
        "Houston",
        "2026-09",
        150_000,
        "CMA",
        None,
        1.40,
    ),
    ("D008", "Exporter D", "SELL", "Houston", "2026-09", 60_000, "FIXED", 93.00, None),
]

TICKETS = {
    "D001": [50_120, 49_870, 50_210],
    "D002": [30_050, 29_940, 30_000],
    "D003": [37_000, 37_000, 37_000],  # 7.5% short of contract: outside +/-5%
    "D004": [40_100, 39_900, 40_050],
    "D005": [49_800, 50_300, 50_050],
    "D006": [29_500, 29_600],
    "D007": [50_000, 49_950, 50_100],
    "D008": [30_010, 29_990],
}

# CMA swaps that settle against the monthly CMA. Positive volume = long.
SWAPS = [
    ("S001", "2026-08", -90_000, 81.60),  # offsets fixed-price purchase D002
    ("S002", "2026-09", 50_000, 92.40),  # only 50k of the 60k fixed sale D008
]

TRANSPORT = [("Midland", "Houston", 0.55), ("Cushing", "Houston", 0.90)]

PLANTED_BREAKS = {
    "D001": "PRICE",  # invoice priced off July CMA instead of August
    "D005": "PRICE",  # invoice uses +0.85 differential; contract says +0.80
    "D006": "VOLUME",  # invoice bills contract 60,000 bbl; tickets total 59,100
    "D007": "MISSING_INVOICE",
}
PLANTED_DELIVERY_ISSUES = {"D003": "UNDER_DELIVERED"}


def monthly_cma(prices):
    frame = prices.assign(month=prices.date.str[:7])
    return frame.groupby("month").cl_front_month_proxy.mean().round(4)


def contract_price(deal, cma):
    if deal["pricing_type"] == "FIXED":
        return deal["fixed_price"]
    return round(cma[deal["delivery_month"]] + deal["differential"], 4)


def build():
    BOOK.mkdir(parents=True, exist_ok=True)
    cma = monthly_cma(pd.read_csv(PRICES))
    deals = pd.DataFrame(
        DEALS,
        columns=[
            "deal_id",
            "counterparty",
            "side",
            "location",
            "delivery_month",
            "contract_bbl",
            "pricing_type",
            "fixed_price",
            "differential",
        ],
    )
    deals["tolerance_pct"] = 5.0
    tickets = pd.DataFrame(
        [
            (f"{deal_id}-T{n}", deal_id, volume)
            for deal_id, volumes in TICKETS.items()
            for n, volume in enumerate(volumes, start=1)
        ],
        columns=["ticket_id", "deal_id", "volume_bbl"],
    )
    delivered = tickets.groupby("deal_id").volume_bbl.sum()

    invoices = []
    for deal in deals.to_dict("records"):
        deal_id = deal["deal_id"]
        if PLANTED_BREAKS.get(deal_id) == "MISSING_INVOICE":
            continue
        price = contract_price(deal, cma)
        volume = int(delivered[deal_id])
        if deal_id == "D001":
            price = round(cma["2026-07"] + deal["differential"], 4)
        elif deal_id == "D005":
            price = round(cma[deal["delivery_month"]] + 0.85, 4)
        elif deal_id == "D006":
            volume = deal["contract_bbl"]
        invoices.append(
            (f"INV-{deal_id}", deal_id, volume, price, round(volume * price, 2))
        )
    invoices = pd.DataFrame(
        invoices,
        columns=["invoice_id", "deal_id", "invoiced_bbl", "invoiced_price", "amount"],
    )
    swaps = pd.DataFrame(
        SWAPS, columns=["swap_id", "delivery_month", "volume_bbl", "fixed_price"]
    )
    transport = pd.DataFrame(
        TRANSPORT, columns=["origin", "destination", "tariff_per_bbl"]
    )
    for name, frame in [
        ("deals", deals),
        ("tickets", tickets),
        ("invoices", invoices),
        ("swaps", swaps),
        ("transport", transport),
    ]:
        frame.to_csv(BOOK / f"{name}.csv", index=False)


if __name__ == "__main__":
    build()
