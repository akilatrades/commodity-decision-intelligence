"""Transparent mass balances and scenario hedges, not plant profit estimates."""

from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class Route:
    ethylene_yield: float
    polymer_yield: float = 0.98
    cracking_cost_cents_lb_ethylene: float = 10
    polymer_cost_cents_lb_pe: float = 6
    coproduct_credit_cents_lb_feed: float = 0

    def __post_init__(self):
        if not all(isfinite(v) for v in vars(self).values()):
            raise ValueError("Finite assumptions required")
        if not 0 < self.ethylene_yield <= 1 or not 0 < self.polymer_yield <= 1:
            raise ValueError("Mass yields must be in (0, 1]")
        if (
            min(
                self.cracking_cost_cents_lb_ethylene,
                self.polymer_cost_cents_lb_pe,
                self.coproduct_credit_cents_lb_feed,
            )
            < 0
        ):
            raise ValueError("Costs and credit must be nonnegative")

    @property
    def feed_lb_per_lb_pe(self):
        return 1 / (self.ethylene_yield * self.polymer_yield)


def margin(feed, ethylene, pe, route):
    if not all(isfinite(x) and x >= 0 for x in [feed, ethylene, pe]):
        raise ValueError("Finite nonnegative prices required, in cents/lb")
    net_feed = feed - route.coproduct_credit_cents_lb_feed
    cracker = (
        ethylene
        - net_feed / route.ethylene_yield
        - route.cracking_cost_cents_lb_ethylene
    )
    polymer = pe - ethylene / route.polymer_yield - route.polymer_cost_cents_lb_pe
    integrated = cracker / route.polymer_yield + polymer
    return dict(
        cracker_proxy_cents_lb_ethylene=cracker,
        polymer_proxy_cents_lb_pe=polymer,
        integrated_proxy_cents_lb_pe=integrated,
        feed_lb_per_lb_pe=route.feed_lb_per_lb_pe,
    )


def hedged_contribution(
    feed,
    ethylene,
    pe,
    route,
    fixed_price,
    benchmark_settle,
    hedge_fraction=1,
    pe_volume_lb=1_000_000,
):
    if not 0 <= hedge_fraction <= 1 or not isfinite(pe_volume_lb) or pe_volume_lb <= 0:
        raise ValueError("Valid volume and hedge fraction required")
    if not all(isfinite(x) and x >= 0 for x in [fixed_price, benchmark_settle]):
        raise ValueError("Finite nonnegative hedge prices required")
    physical = (
        margin(feed, ethylene, pe, route)["integrated_proxy_cents_lb_pe"]
        * pe_volume_lb
        / 100
    )
    feed_volume = pe_volume_lb * route.feed_lb_per_lb_pe
    # A consumer buys feedstock: a LONG fixed-price swap gains when its index rises.
    swap = feed_volume * hedge_fraction * (benchmark_settle - fixed_price) / 100
    return dict(
        physical_contribution_usd=physical,
        swap_pnl_usd=swap,
        hedged_contribution_usd=physical + swap,
        feed_volume_lb=feed_volume,
    )
