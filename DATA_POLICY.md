# Data Policy

## Purpose

A commodity analytics product can only be trusted if users know where the data came from and whether the project has the right to use it.

This project will keep different classes of data clearly separated.

---

## 1. Synthetic data

Synthetic data is invented specifically for testing and demonstration.

Example:

```text
Expected production: 100,000 bbl
Reference WTI price: $70/bbl
Hedge ratio: 75%
```

Synthetic data will be used first because it gives us a known answer that can be calculated manually.

Synthetic values must never be presented as historical market observations.

---

## 2. Public data

Public data may later include government or other sources whose terms permit the intended use.

Every public series added to the project should have metadata describing:

- source,
- series identifier,
- frequency,
- original unit,
- normalized unit,
- retrieval time,
- transformation applied.

Public availability does not automatically mean unrestricted commercial redistribution.

---

## 3. Licensed market data

Exchange prices, professional vendor data, and other licensed datasets must be treated separately from public data.

The project will not assume that data can be redistributed simply because it can be viewed online or downloaded through a user account.

Before licensed data is used in a commercial product, the relevant display, non-display, derived-data, storage, and redistribution rights must be reviewed.

No licensed exchange data is required for v0.1.

---

## 4. Customer-proprietary data

A future enterprise version may ingest customer positions, hedges, operational assumptions, or other confidential data.

Customer data must never be committed to the public repository.

A production implementation would eventually require controls such as:

- authentication,
- role-based access,
- encryption,
- audit logging,
- retention rules,
- environment separation,
- secrets management,
- contractual data-handling terms.

Those controls are outside the current prototype.

---

## 5. Repository rule

The public repository may contain:

- source code,
- synthetic sample data,
- documentation,
- tests,
- non-restricted generated examples.

It should not contain:

- API keys,
- passwords,
- customer information,
- confidential company files,
- proprietary vendor datasets,
- licensed market data that cannot be redistributed.

---

## 6. Data lineage principle

Every important analytical result should eventually be answerable through:

```text
Result
  ↓
Calculation
  ↓
Normalized input
  ↓
Raw input
  ↓
Source / assumption
```

This is the foundation for auditability.
