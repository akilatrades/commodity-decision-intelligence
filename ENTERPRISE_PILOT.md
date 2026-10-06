# Enterprise Pilot Definition

## Objective

Design the first product around a **large-enterprise crude market-risk workflow**, while keeping the pilot narrow enough to build, test, and deploy safely.

The product is not intended to replace an ETRM. It is an analytical layer that sits above existing systems and helps a risk or commercial analytics team understand exposure, hedge coverage, scenario impact, and the drivers behind the result.

## Primary enterprise user

The first enterprise persona is a:

**Crude Market Risk / Supply & Trading Analytics user**

Typical responsibilities may include:

- reviewing physical and financial exposure,
- checking hedge coverage,
- running stress and scenario analysis,
- explaining major risk drivers,
- preparing management commentary,
- reconciling outputs across spreadsheets and existing systems.

The first buyer/champion could be a Market Risk Manager, Commodity Risk Manager, or Supply & Trading Analytics lead.

## Pilot business problem

A crude portfolio contains physical exposure and futures hedges.

The team wants to answer:

> If crude prices or key assumptions change, what happens to the portfolio, which positions drive the result, and can every output be traced back to its inputs?

## Pilot scope

The first enterprise-shaped pilot will intentionally remain small:

- one commodity: WTI crude oil,
- one fictional business unit,
- one reporting currency: USD,
- physical crude exposure,
- WTI futures hedges,
- controlled scenario shocks,
- exposure and hedge attribution,
- deterministic calculations,
- downloadable or structured result output,
- full traceability from result to input.

Synthetic data will be used first.

## Initial inputs

The first controlled dataset should eventually represent:

### Physical exposure

- exposure ID,
- business unit,
- commodity,
- location,
- delivery month,
- expected volume,
- volume unit,
- reference price.

### Hedge exposure

- hedge ID,
- hedge instrument,
- contract month,
- long/short direction,
- number of contracts,
- contract multiplier,
- reference futures price.

### Scenario

- scenario ID,
- scenario name,
- WTI price shock,
- optional volume shock later,
- optional basis shock later.

## Initial outputs

The pilot should calculate and report:

- gross physical exposure,
- hedged volume,
- unhedged volume,
- hedge percentage,
- physical scenario impact,
- futures hedge scenario impact,
- net scenario impact,
- largest exposure driver,
- assumptions used,
- calculation trace.

## Enterprise design principles

Even during the prototype, the architecture should preserve:

### Auditability
Every material output should be traceable to the exact input and formula that produced it.

### Determinism
The same inputs and scenario must return the same numerical result.

### Separation of data classes
Synthetic, public, licensed, and customer-proprietary data must remain distinct.

### Validation
The system should reject invalid or incomplete data instead of silently fixing or guessing.

### Explainability
Users should be able to understand why a result changed.

### Integration readiness
Inputs should be modeled so that a CSV used in the prototype could later be replaced by an ETRM export, API, database, or approved market-data feed without redesigning the analytical core.

## What the pilot does not attempt

The initial pilot will not include:

- enterprise-wide deployment,
- live ETRM integration,
- real-time exchange data,
- options or Greeks,
- complex physical contracts,
- crack-spread or refinery optimization,
- accounting,
- trade capture,
- settlement,
- regulatory reporting,
- AI-generated trading recommendations.

## Pilot success criteria

A successful first pilot should prove that:

1. the system reproduces hand-calculated exposure and hedge results,
2. a scenario can be run consistently and quickly,
3. the result can be attributed to physical and hedge components,
4. invalid data is caught clearly,
5. every result has an auditable calculation path,
6. the input model can later accept enterprise exports without changing the calculation engine.

## Commercial hypothesis

The product may be valuable if it can reduce manual spreadsheet work and make scenario analysis faster, more consistent, and more auditable.

A future enterprise proof-of-value should measure outcomes such as:

- time required to prepare a scenario,
- number of manual reconciliation steps,
- number of unsupported spreadsheet transformations,
- speed of identifying the largest risk driver,
- percentage of outputs with complete data lineage.

The initial software build will not claim these improvements until they are measured with real users.
