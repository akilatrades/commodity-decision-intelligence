# Public benchmark provenance

The input file transcribes a small historical benchmark table from Westlake's public SEC earnings exhibits. Each row carries its source and publication date. Prices are quarterly averages in cents/lb: Mont Belvieu purity ethane; Mont Belvieu non-TET propane; North American spot ethylene; domestic net-transaction and export LDPE general-purpose film benchmarks. These are industry benchmarks attributed by the issuer to IHS Markit, not actual company realizations or a comprehensive licensed price feed.

| Quarters used | Public exhibit | Publication date |
|---|---|---|
| 2019Q1–Q3 | [2020Q1 earnings release](https://www.sec.gov/Archives/edgar/data/1262823/000126282320000013/ex991200331earningsrel.htm) | 2020-05-04 |
| 2019Q4–2020Q4 | [2020 annual earnings release](https://www.sec.gov/Archives/edgar/data/1262823/000126282321000014/ex991_201231earningsreleas.htm) | 2021-02-23 |
| 2021Q1–Q4 | [2021 annual presentation](https://www.sec.gov/Archives/edgar/data/1262823/000126282322000011/ex992_20211231investorpr.htm) | 2022-02-22 |
| 2022Q1 | [2022Q1 presentation](https://www.sec.gov/Archives/edgar/data/1262823/000126282322000019/ex992_20220331wlkearning.htm) | 2022-05-03 |

This uses the specified later disclosure vintages, not a point-in-time tradeable dataset. For example, 2020Q1 export LDPE is 39.4 in the 2020 annual release versus 38.9 in the earlier Q1 release. No values have been interpolated. A quarter's average is not available at the quarter's start; nothing here trades on that assumption.

The [2022Q2 presentation](https://www.sec.gov/Archives/edgar/data/1262823/000126282322000039/ex992_20220630wlkearning.htm) states that average quarterly industry prices are no longer being provided. The sample therefore stops at 2022Q1. It is deliberately presented as a historical case study, not current market monitoring.

No proprietary employer data, internal plant benchmarks or client information is included. Yield, conversion cost and coproduct assumptions belong to the model, not these sources.
