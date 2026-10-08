"""Reproduce the public historical case study and explicitly assumed scenarios."""
import hashlib
import json
from dataclasses import asdict
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from model import Route, hedged_contribution, margin


def main():
    source = Path("data/public_quarterly_prices.csv")
    prices = pd.read_csv(source)
    if prices.quarter.duplicated().any() or prices.isna().any().any():
        raise ValueError("Unique complete quarterly data required")
    out = Path("outputs")
    out.mkdir(exist_ok=True)
    routes = {"ethane": Route(.80), "propane": Route(.42)}
    rows = []
    for row in prices.itertuples():
        for name, route in routes.items():
            for market in ["domestic", "export"]:
                rows.append(dict(quarter=row.quarter, route=name, market=market,
                                 **margin(getattr(row, f"{name}_cents_lb"), row.ethylene_cents_lb,
                                          getattr(row, f"ldpe_{market}_cents_lb"), route)))
    history = pd.DataFrame(rows)
    history.to_csv(out / "margin_history.csv", index=False)
    history["regime"] = history.quarter.str[:4].map({"2019": "2019", "2020": "2020", "2021": "2021–2022Q1", "2022": "2021–2022Q1"})
    history.groupby(["regime", "route", "market"]).integrated_proxy_cents_lb_pe.agg(["count", "mean", "min", "max"]).to_csv(out / "regimes.csv")
    base = prices.iloc[-1]
    scenarios = []
    for name, route in routes.items():
        feed = base[f"{name}_cents_lb"]
        for feed_move in [-.2, 0, .2]:
            for pe_move in [-.15, 0, .15]:
                for basis in [0, 2]:
                    for fraction in [0, .5, 1]:
                        benchmark = feed * (1 + feed_move)
                        scenarios.append(dict(route=name, feed_move=feed_move, pe_move=pe_move,
                                              basis_cents_lb_feed=basis, hedge_fraction=fraction,
                                              **hedged_contribution(benchmark + basis, base.ethylene_cents_lb,
                                                  base.ldpe_domestic_cents_lb * (1 + pe_move), route,
                                                  feed, benchmark, fraction)))
    pd.DataFrame(scenarios).to_csv(out / "hedge_scenarios.csv", index=False)
    sensitivity = []
    for name, yields in [("ethane", [.75, .80, .85]), ("propane", [.35, .42, .50])]:
        for yield_ in yields:
            for credit in [0, 5, 10, 15]:
                route = Route(yield_, coproduct_credit_cents_lb_feed=credit)
                sensitivity.append(dict(route=name, ethylene_yield=yield_, credit_cents_lb_feed=credit,
                                        **margin(base[f"{name}_cents_lb"], base.ethylene_cents_lb,
                                                 base.ldpe_domestic_cents_lb, route)))
    pd.DataFrame(sensitivity).to_csv(out / "yield_credit_sensitivity.csv", index=False)
    fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
    for col, label in [("ethane_cents_lb", "Ethane"), ("propane_cents_lb", "Propane"),
                       ("ldpe_domestic_cents_lb", "Domestic LDPE"), ("ldpe_export_cents_lb", "Export LDPE")]:
        axes[0].plot(prices.quarter, prices[col], marker=".", label=label)
    for name in routes:
        selected = history[(history.route == name) & (history.market == "domestic")]
        axes[1].plot(selected.quarter, selected.integrated_proxy_cents_lb_pe, marker=".", label=f"{name}: zero coproduct credit")
    axes[0].set(ylabel="Benchmark cents/lb", title="Public feedstock and LDPE benchmarks, 2019Q1–2022Q1")
    axes[1].set(ylabel="Contribution proxy cents/lb PE", title="Illustrative yields and conversion costs; excludes plant fixed costs")
    axes[1].axhline(0, color="black", lw=.7)
    for ax in axes:
        ax.legend(fontsize=8)
    plt.xticks(rotation=45)
    fig.tight_layout()
    fig.savefig(out / "feedstock_to_pe.svg")
    plt.close(fig)
    (out / "assumptions.json").write_text(json.dumps(dict(
        input_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
        routes={k: asdict(v) for k, v in routes.items()},
        units="Prices cents/lb; scenario dollars divide by 100",
        benchmark="IHS Markit industry benchmarks disclosed by Westlake, not its realized prices",
        scope="Historical 13-quarter case study, not a current margin monitor or trading backtest",
        scenario="2022Q1 price used as ASSUMED fixed swap strike, not an observed executable quote",
        omissions=["fixed costs", "actual energy consumption", "freight", "grade/location basis", "working capital", "hedge fees/collateral", "plant-specific coproduct slate"],
        coproduct_warning="Zero credit base case intentionally does not establish comparative route profitability"
    ), indent=2) + "\n")
    print(history.groupby(["regime", "route", "market"]).integrated_proxy_cents_lb_pe.mean().to_string())


if __name__ == "__main__":
    main()
