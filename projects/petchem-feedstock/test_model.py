import pytest

from model import Route, hedged_contribution, margin


def test_integrated_mass_balance():
    route = Route(.8)
    result = margin(10, 25, 60, route)
    direct = 60 - (10 / .8 + 10) / .98 - 6
    assert result["integrated_proxy_cents_lb_pe"] == pytest.approx(direct)
    assert result["feed_lb_per_lb_pe"] == pytest.approx(1 / (.8 * .98))


def test_full_feed_hedge_cancels_feed_move_but_not_pe_or_basis():
    route = Route(.8)
    base = hedged_contribution(10, 25, 60, route, 10, 10)
    up = hedged_contribution(15, 25, 60, route, 10, 15)
    assert up["swap_pnl_usd"] > 0
    assert up["hedged_contribution_usd"] == pytest.approx(base["hedged_contribution_usd"])
    pe_down = hedged_contribution(15, 25, 54, route, 10, 15)
    assert base["hedged_contribution_usd"] - pe_down["hedged_contribution_usd"] == pytest.approx(60000)
    basis = hedged_contribution(17, 25, 60, route, 10, 15)
    assert up["hedged_contribution_usd"] - basis["hedged_contribution_usd"] == pytest.approx(20000 / (.8 * .98))


def test_coproduct_credit_and_invalid_yield():
    before = margin(20, 30, 60, Route(.42))
    after = margin(20, 30, 60, Route(.42, coproduct_credit_cents_lb_feed=5))
    assert after["integrated_proxy_cents_lb_pe"] - before["integrated_proxy_cents_lb_pe"] == pytest.approx(5 / (.42 * .98))
    with pytest.raises(ValueError):
        Route(0)
