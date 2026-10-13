import shutil

import pandas as pd
import pytest
from book import BOOK, load, report
from build_book import PLANTED_BREAKS, PLANTED_DELIVERY_ISSUES


@pytest.fixture(scope="module")
def con():
    return load()


def test_cma_and_contract_prices(con):
    prices = pd.read_csv("data/cl_front_month_proxy_2026q3.csv")
    august = prices[prices.date.str.startswith("2026-08")].cl_front_month_proxy
    cma = con.execute("SELECT cma FROM cma WHERE month = '2026-08'").fetchone()[0]
    assert cma == pytest.approx(round(august.mean(), 4))
    fixed, floating = con.execute(
        "SELECT contract_price FROM deal_prices WHERE deal_id IN ('D002', 'D001') "
        "ORDER BY deal_id DESC"
    ).fetchall()
    assert fixed[0] == 81.90
    assert floating[0] == pytest.approx(round(cma + 0.85, 4))


def test_reconciliation_finds_exactly_the_planted_breaks(con):
    recon = report(con, "invoice_reconciliation")
    breaks = recon[recon.status != "MATCHED"].set_index("deal_id").status.to_dict()
    assert breaks == PLANTED_BREAKS


def test_break_amounts_are_explained(con):
    recon = report(con, "invoice_reconciliation").set_index("deal_id")
    # D005: invoice applies +0.85 instead of +0.80 on 150,150 bbl
    assert recon.loc["D005", "amount_difference"] == pytest.approx(0.05 * 150_150)
    # D006: bills 60,000 contract barrels; tickets total 59,100
    d006 = recon.loc["D006"]
    assert d006.amount_difference == pytest.approx(900 * d006.contract_price, abs=0.01)


def test_delivery_tolerance(con):
    check = report(con, "delivery_check")
    flagged = check[check.status != "WITHIN_TOLERANCE"]
    assert flagged.set_index("deal_id").status.to_dict() == PLANTED_DELIVERY_ISSUES
    d003 = check.set_index("deal_id").loc["D003"]
    assert d003.difference_pct == -7.5


def test_positions_show_unhedged_fixed_sale(con):
    positions = report(con, "positions").set_index("delivery_month")
    assert positions.loc["2026-08", "net_flat_price_bbl"] == 0
    assert positions.loc["2026-09", "fixed_price_bbl"] == -60_000
    assert positions.loc["2026-09", "net_flat_price_bbl"] == -10_000
    assert (positions.net_physical_bbl == 0).all()


def test_pnl_adds_up(con):
    pnl = report(con, "pnl").set_index("delivery_month")
    cma = dict(con.execute("SELECT month, cma FROM cma").fetchall())
    for month, row in pnl.iterrows():
        expected = (
            row.sales_revenue
            - row.purchase_cost
            - row.transport_cost
            + row.swap_pnl
            + row.unsold_bbl * cma[month]
        )
        assert row.book_pnl == pytest.approx(expected, abs=0.02)
    assert pnl.loc["2026-09", "swap_pnl"] == pytest.approx(
        (cma["2026-09"] - 92.40) * 50_000, abs=0.01
    )


def test_hand_built_deal(tmp_path):
    book = tmp_path / "book"
    shutil.copytree(BOOK, book)
    pd.DataFrame(
        [("X1", "Test", "BUY", "Midland", "2026-08", 1000, "FIXED", 70.0, None, 5.0)],
        columns=pd.read_csv(BOOK / "deals.csv").columns,
    ).to_csv(book / "deals.csv", index=False)
    pd.DataFrame(
        [("X1-T1", "X1", 1000)], columns=["ticket_id", "deal_id", "volume_bbl"]
    ).to_csv(book / "tickets.csv", index=False)
    pd.DataFrame(
        [("I1", "X1", 1000, 70.0, 70_000.0)],
        columns=["invoice_id", "deal_id", "invoiced_bbl", "invoiced_price", "amount"],
    ).to_csv(book / "invoices.csv", index=False)
    con = load(book=book)
    row = report(con, "invoice_reconciliation").iloc[0]
    assert (row.expected_amount, row.status) == (70_000.0, "MATCHED")


def test_month_without_prices_fails(tmp_path):
    prices = pd.read_csv("data/cl_front_month_proxy_2026q3.csv")
    thin = tmp_path / "prices.csv"
    prices[~prices.date.str.startswith("2026-09")].to_csv(thin, index=False)
    with pytest.raises(ValueError):
        load(prices=thin)
