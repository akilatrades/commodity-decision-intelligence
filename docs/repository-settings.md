# Repository names, descriptions and topics

Proposed GitHub settings, prepared October 8, 2026. **Pending application through GitHub settings or an authenticated GitHub CLI.** Committing this file does not change repository metadata.

The intended rename is `commodity-decision-intelligence` → `petchem-feedstock-margins`. Keep the current project directory and earlier package intact; renaming the GitHub repository does not require renaming Python imports.

| Repository | About description | Topics |
|---|---|---|
| `wti-producer-hedge-simulator` | WTI producer hedging with futures, collars and basis risk, plus crude storage carry linked to Cushing inventories. | `energy-trading`, `commodities`, `hedging`, `risk-management`, `wti`, `python` |
| `energy-commodity-var-engine` | VaR and Expected Shortfall for a refiner hedge book, with EWMA filtering, backtests and contract-roll diagnostics. | `energy-trading`, `commodities`, `risk-management`, `var`, `expected-shortfall`, `backtesting`, `python` |
| `petchem-feedstock-margins` (currently `commodity-decision-intelligence`) | Public ethane, propane and polyethylene benchmarks, with mass balances, margin scenarios and feedstock hedge analysis. | `petrochemicals`, `polyethylene`, `commodities`, `hedging`, `risk-management`, `python` |
| `nfl-dfs-projection-analysis` | NFL projection analysis exploring forecast uncertainty and prediction performance. | `nfl`, `sports-analytics`, `forecasting`, `python` |
| `akilatrades` | Background in polyolefins benchmarking; projects in energy trading, commodity risk and quantitative analysis. | `profile-readme`, `energy-trading`, `commodities`, `risk-management`, `petrochemicals` |

The storage study is a directory inside the WTI repository, so it has no separate GitHub About panel.

## Apply through GitHub

On each repository's Code page, use the gear beside **About** to enter the description and topics above. For the petchem rename, open **Settings → General → Repository name**, enter `petchem-feedstock-margins`, and choose **Rename**.

## Apply with GitHub CLI

The following commands work as separate lines in PowerShell or Bash with [GitHub CLI](https://cli.github.com/) installed and authenticated to an account that can administer these repositories. They add the listed topics and preserve any other topics. Run the rename once, after the description/topic updates succeed.

```text
gh repo edit akilatrades/wti-producer-hedge-simulator --description "WTI producer hedging with futures, collars and basis risk, plus crude storage carry linked to Cushing inventories." --add-topic energy-trading,commodities,hedging,risk-management,wti,python
gh repo edit akilatrades/energy-commodity-var-engine --description "VaR and Expected Shortfall for a refiner hedge book, with EWMA filtering, backtests and contract-roll diagnostics." --add-topic energy-trading,commodities,risk-management,var,expected-shortfall,backtesting,python
gh repo edit akilatrades/commodity-decision-intelligence --description "Public ethane, propane and polyethylene benchmarks, with mass balances, margin scenarios and feedstock hedge analysis." --add-topic petrochemicals,polyethylene,commodities,hedging,risk-management,python
gh repo edit akilatrades/nfl-dfs-projection-analysis --description "NFL projection analysis exploring forecast uncertainty and prediction performance." --add-topic nfl,sports-analytics,forecasting,python
gh repo edit akilatrades/akilatrades --description "Background in polyolefins benchmarking; projects in energy trading, commodity risk and quantitative analysis." --add-topic profile-readme,energy-trading,commodities,risk-management,petrochemicals
gh repo rename petchem-feedstock-margins --repo akilatrades/commodity-decision-intelligence --yes
```

After the rename, update local Git remotes and portfolio links to the new canonical URL.

CLI references: [edit](https://cli.github.com/manual/gh_repo_edit) · [rename](https://cli.github.com/manual/gh_repo_rename).
