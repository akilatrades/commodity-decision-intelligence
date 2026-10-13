"""Load the physical crude book into SQLite and run the SQL reports.

Run from this directory: python book.py
"""

import sqlite3
from pathlib import Path

import pandas as pd

SQL = Path("sql")
DATA = Path("data")
BOOK = DATA / "book"
REPORTS = [
    "invoice_reconciliation",
    "delivery_check",
    "positions",
    "pnl",
]


def load(path=":memory:", book=BOOK, prices=DATA / "cl_front_month_proxy_2026q3.csv"):
    con = sqlite3.connect(path)
    con.execute("PRAGMA foreign_keys = ON")
    con.executescript((SQL / "schema.sql").read_text())
    tables = {
        "cl_daily": prices,
        "deals": book / "deals.csv",
        "tickets": book / "tickets.csv",
        "invoices": book / "invoices.csv",
        "swaps": book / "swaps.csv",
        "transport": book / "transport.csv",
    }
    for table, csv in tables.items():
        frame = pd.read_csv(csv)
        frame = frame.astype(object).where(frame.notna(), None)
        columns = ", ".join(frame.columns)
        marks = ", ".join("?" for _ in frame.columns)
        con.executemany(
            f"INSERT INTO {table} ({columns}) VALUES ({marks})",
            frame.itertuples(index=False, name=None),
        )
    con.executescript((SQL / "views.sql").read_text())
    con.commit()
    check_complete_months(con)
    return con


def check_complete_months(con):
    """Every deal month needs a CMA built from a full month of prices."""
    missing = con.execute(
        """
        SELECT DISTINCT d.delivery_month
        FROM deals AS d
        LEFT JOIN cma AS c ON c.month = d.delivery_month
        WHERE c.cma IS NULL OR c.trading_days < 15
        """
    ).fetchall()
    if missing:
        raise ValueError(f"No complete CMA for {[m for (m,) in missing]}")


def report(con, name):
    return pd.read_sql_query((SQL / f"{name}.sql").read_text(), con)


def main():
    out = Path("outputs")
    out.mkdir(exist_ok=True)
    con = load()
    pd.read_sql_query("SELECT * FROM cma ORDER BY month", con).to_csv(
        out / "cma.csv", index=False
    )
    for name in REPORTS:
        frame = report(con, name)
        frame.to_csv(out / f"{name}.csv", index=False)
        print(f"\n{name}\n{frame.to_string(index=False)}")


if __name__ == "__main__":
    main()
