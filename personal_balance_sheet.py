#!/usr/bin/env python3
"""Simple personal finance balance sheet and free cash flow calculator."""

from __future__ import annotations

import argparse
from dataclasses import dataclass

SUPPORTED_CURRENCIES = {
    "EUR": "€",
    "USD": "$",
    "GBP": "£",
    "INR": "₹",
    "JPY": "¥",
    "CAD": "C$",
    "AUD": "A$",
}


@dataclass
class BalanceSheet:
    age: int
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


def prompt_amount(label: str, currency_symbol: str) -> float:
    while True:
        raw = input(f"{label}: {currency_symbol}").strip()
        normalized = raw.replace(",", "").replace(" ", "")
        for symbol in set(SUPPORTED_CURRENCIES.values()):
            normalized = normalized.replace(symbol, "")
        try:
            value = float(normalized)
        except ValueError:
            print("Please enter a valid number (for example: 1200 or 1200.50).")
            continue

        if value < 0:
            print("Please enter 0 or a positive amount.")
            continue

        return value


def prompt_yes_no(label: str, default: bool = False) -> bool:
    suffix = "Y/n" if default else "y/N"
    while True:
        raw = input(f"{label} ({suffix}): ").strip().lower()
        if raw == "":
            return default
        if raw in {"y", "yes"}:
            return True
        if raw in {"n", "no"}:
            return False
        print("Please enter y/yes or n/no.")


def prompt_age() -> int:
    while True:
        raw = input("Your age (focused range is 22-35): ").strip()
        try:
            age = int(raw)
        except ValueError:
            print("Please enter a whole number for age.")
            continue

        if age < 18 or age > 100:
            print("Please enter a realistic age between 18 and 100.")
            continue

        return age


def collect_inputs(currency_symbol: str) -> BalanceSheet:
    print("\nEnter your amounts below. Use monthly values for income and expenses.\n")
    age = prompt_age()
    if age < 22 or age > 35:
        print("Note: This tool is optimized for ages 22-35, but it still works for you.\n")

    include_retirement = prompt_yes_no(
        "Do you currently have retirement accounts (401(k), IRA, etc.)?",
        default=False,
    )
    include_property = prompt_yes_no(
        "Do you own property (house/apartment/land)?",
        default=False,
    )

    retirement_accounts = (
        prompt_amount("Retirement accounts (401(k), IRA, etc.)", currency_symbol)
        if include_retirement
        else 0.0
    )
    real_estate_value = (
        prompt_amount("Real estate market value", currency_symbol)
        if include_property
        else 0.0
    )
    mortgage_balance = (
        prompt_amount("Mortgage balance", currency_symbol)
        if include_property
        else 0.0
    )

    return BalanceSheet(
        age=age,
        cash_and_bank=prompt_amount("Cash + bank accounts", currency_symbol),
        investments=prompt_amount(
            "Investments (brokerage, stocks, ETFs, etc.)", currency_symbol
        ),
        retirement_accounts=retirement_accounts,
        real_estate_value=real_estate_value,
        other_assets=prompt_amount("Other assets", currency_symbol),
        credit_card_debt=prompt_amount("Credit card debt", currency_symbol),
        loans=prompt_amount("Loans (student, auto, personal)", currency_symbol),
        mortgage_balance=mortgage_balance,
        other_liabilities=prompt_amount("Other liabilities", currency_symbol),
        monthly_income=prompt_amount("Monthly take-home income", currency_symbol),
        monthly_expenses=prompt_amount("Monthly living expenses", currency_symbol),
        monthly_debt_payments=prompt_amount(
            "Monthly debt payments (minimums + EMI)", currency_symbol
        ),
    )


def as_currency(amount: float, currency_symbol: str) -> str:
    return f"{currency_symbol}{amount:,.2f}"


def print_report(sheet: BalanceSheet, currency_code: str, currency_symbol: str) -> None:
    print("\n" + "=" * 58)
    print("PERSONAL FINANCE BALANCE SHEET")
    print("=" * 58)
    print(f"Currency: {currency_code} ({currency_symbol})")
    print(f"Age profile: {sheet.age}")

    print("\nASSETS")
    print(f"  Cash + bank accounts      : {as_currency(sheet.cash_and_bank, currency_symbol)}")
    print(f"  Investments               : {as_currency(sheet.investments, currency_symbol)}")
    print(
        f"  Retirement accounts       : {as_currency(sheet.retirement_accounts, currency_symbol)}"
    )
    print(f"  Real estate               : {as_currency(sheet.real_estate_value, currency_symbol)}")
    print(f"  Other assets              : {as_currency(sheet.other_assets, currency_symbol)}")
    print(f"  Total Assets              : {as_currency(sheet.total_assets, currency_symbol)}")

    print("\nLIABILITIES")
    print(f"  Credit card debt          : {as_currency(sheet.credit_card_debt, currency_symbol)}")
    print(f"  Loans                     : {as_currency(sheet.loans, currency_symbol)}")
    print(f"  Mortgage balance          : {as_currency(sheet.mortgage_balance, currency_symbol)}")
    print(f"  Other liabilities         : {as_currency(sheet.other_liabilities, currency_symbol)}")
    print(f"  Total Liabilities         : {as_currency(sheet.total_liabilities, currency_symbol)}")

    print("\nNET WORTH")
    print(f"  Net Worth (Assets - Liabilities): {as_currency(sheet.net_worth, currency_symbol)}")

    print("\nFREE CASH FLOW")
    print(
        f"  Monthly Free Cash Flow    : {as_currency(sheet.monthly_free_cash_flow, currency_symbol)}"
    )
    print(
        f"  Yearly Free Cash Flow     : {as_currency(sheet.yearly_free_cash_flow, currency_symbol)}"
    )

    if sheet.monthly_free_cash_flow < 0:
        print("\nNote: Your free cash flow is negative. Review expenses and debt payments.")
    else:
        print("\nGreat! You are generating positive free cash flow.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a simple personal finance balance sheet and calculate free cash flow."
    )
    parser.add_argument(
        "--quick-example",
        action="store_true",
        help="Run with sample values to preview the output without entering data.",
    )
    parser.add_argument(
        "--currency",
        choices=sorted(SUPPORTED_CURRENCIES.keys()),
        default="EUR",
        help="Currency code for display. Default is EUR.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    currency_symbol = SUPPORTED_CURRENCIES[args.currency]

    if args.quick_example:
        sheet = BalanceSheet(
            age=28,
            cash_and_bank=8000,
            investments=25000,
            retirement_accounts=0,
            real_estate_value=0,
            other_assets=3500,
            credit_card_debt=1200,
            loans=6000,
            mortgage_balance=0,
            other_liabilities=500,
            monthly_income=5500,
            monthly_expenses=3100,
            monthly_debt_payments=800,
        )
    else:
        sheet = collect_inputs(currency_symbol)

    print_report(sheet, args.currency, currency_symbol)


if __name__ == "__main__":
    main()
