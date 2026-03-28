#!/usr/bin/env python3
"""Simple personal finance balance sheet and free cash flow calculator."""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass
class BalanceSheet:
    cash_and_bank: float
    investments: float
    retirement_accounts: float
    real_estate_value: float
    other_assets: float
    credit_card_debt: float
    loans: float
    mortgage_balance: float
    other_liabilities: float
    monthly_income: float
    monthly_expenses: float
    monthly_debt_payments: float

    @property
    def total_assets(self) -> float:
        return (
            self.cash_and_bank
            + self.investments
            + self.retirement_accounts
            + self.real_estate_value
            + self.other_assets
        )

    @property
    def total_liabilities(self) -> float:
        return (
            self.credit_card_debt
            + self.loans
            + self.mortgage_balance
            + self.other_liabilities
        )

    @property
    def net_worth(self) -> float:
        return self.total_assets - self.total_liabilities

    @property
    def monthly_free_cash_flow(self) -> float:
        return self.monthly_income - self.monthly_expenses - self.monthly_debt_payments

    @property
    def yearly_free_cash_flow(self) -> float:
        return self.monthly_free_cash_flow * 12


def prompt_amount(label: str) -> float:
    while True:
        raw = input(f"{label}: $").strip().replace(",", "")
        try:
            value = float(raw)
            if value < 0:
                print("Please enter 0 or a positive amount.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number (for example: 1200 or 1200.50).")


def collect_inputs() -> BalanceSheet:
    print("\nEnter your amounts below. Use monthly values for income and expenses.\n")

    return BalanceSheet(
        cash_and_bank=prompt_amount("Cash + bank accounts"),
        investments=prompt_amount("Investments (brokerage, stocks, ETFs, etc.)"),
        retirement_accounts=prompt_amount("Retirement accounts (401(k), IRA, etc.)"),
        real_estate_value=prompt_amount("Real estate market value"),
        other_assets=prompt_amount("Other assets"),
        credit_card_debt=prompt_amount("Credit card debt"),
        loans=prompt_amount("Loans (student, auto, personal)"),
        mortgage_balance=prompt_amount("Mortgage balance"),
        other_liabilities=prompt_amount("Other liabilities"),
        monthly_income=prompt_amount("Monthly take-home income"),
        monthly_expenses=prompt_amount("Monthly living expenses"),
        monthly_debt_payments=prompt_amount("Monthly debt payments (minimums + EMI)"),
    )


def as_currency(amount: float) -> str:
    return f"${amount:,.2f}"


def print_report(sheet: BalanceSheet) -> None:
    print("\n" + "=" * 58)
    print("PERSONAL FINANCE BALANCE SHEET")
    print("=" * 58)

    print("\nASSETS")
    print(f"  Cash + bank accounts      : {as_currency(sheet.cash_and_bank)}")
    print(f"  Investments               : {as_currency(sheet.investments)}")
    print(f"  Retirement accounts       : {as_currency(sheet.retirement_accounts)}")
    print(f"  Real estate               : {as_currency(sheet.real_estate_value)}")
    print(f"  Other assets              : {as_currency(sheet.other_assets)}")
    print(f"  Total Assets              : {as_currency(sheet.total_assets)}")

    print("\nLIABILITIES")
    print(f"  Credit card debt          : {as_currency(sheet.credit_card_debt)}")
    print(f"  Loans                     : {as_currency(sheet.loans)}")
    print(f"  Mortgage balance          : {as_currency(sheet.mortgage_balance)}")
    print(f"  Other liabilities         : {as_currency(sheet.other_liabilities)}")
    print(f"  Total Liabilities         : {as_currency(sheet.total_liabilities)}")

    print("\nNET WORTH")
    print(f"  Net Worth (Assets - Liabilities): {as_currency(sheet.net_worth)}")

    print("\nFREE CASH FLOW")
    print(f"  Monthly Free Cash Flow    : {as_currency(sheet.monthly_free_cash_flow)}")
    print(f"  Yearly Free Cash Flow     : {as_currency(sheet.yearly_free_cash_flow)}")

    if sheet.monthly_free_cash_flow < 0:
        print("\nNote: Your free cash flow is negative. Review expenses and debt payments.")
    else:
        print("\nGreat! You are generating positive free cash flow.")



def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Create a simple personal finance balance sheet and calculate free cash flow."
        )
    )
    parser.add_argument(
        "--quick-example",
        action="store_true",
        help="Run with sample values to preview the output without entering data.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.quick_example:
        sheet = BalanceSheet(
            cash_and_bank=8000,
            investments=25000,
            retirement_accounts=42000,
            real_estate_value=180000,
            other_assets=5000,
            credit_card_debt=1200,
            loans=6000,
            mortgage_balance=120000,
            other_liabilities=1000,
            monthly_income=5500,
            monthly_expenses=3100,
            monthly_debt_payments=800,
        )
    else:
        sheet = collect_inputs()

    print_report(sheet)


if __name__ == "__main__":
    main()
