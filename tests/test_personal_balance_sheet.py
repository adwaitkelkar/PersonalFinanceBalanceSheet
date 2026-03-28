import io
import unittest
from unittest.mock import patch

import personal_balance_sheet as pbs


class BalanceSheetTests(unittest.TestCase):
    def test_calculations(self):
        sheet = pbs.BalanceSheet(
            age=30,
            cash_and_bank=1000,
            investments=2000,
            retirement_accounts=0,
            real_estate_value=0,
            other_assets=500,
            credit_card_debt=300,
            loans=200,
            mortgage_balance=0,
            other_liabilities=100,
            monthly_income=4000,
            monthly_expenses=2500,
            monthly_debt_payments=500,
        )

        self.assertEqual(sheet.total_assets, 3500)
        self.assertEqual(sheet.total_liabilities, 600)
        self.assertEqual(sheet.net_worth, 2900)
        self.assertEqual(sheet.monthly_free_cash_flow, 1000)
        self.assertEqual(sheet.yearly_free_cash_flow, 12000)

    def test_currency_formatting(self):
        self.assertEqual(pbs.as_currency(1234.5, "€"), "€1,234.50")

    def test_prompt_amount_allows_symbols_and_commas(self):
        with patch("builtins.input", side_effect=["€1,200.50"]):
            value = pbs.prompt_amount("Cash", "€")
        self.assertEqual(value, 1200.50)

    def test_quick_example_runs(self):
        with patch("sys.argv", ["personal_balance_sheet.py", "--quick-example", "--currency", "USD"]):
            with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
                pbs.main()
                output = mock_stdout.getvalue()

        self.assertIn("PERSONAL FINANCE BALANCE SHEET", output)
        self.assertIn("Monthly Free Cash Flow", output)
        self.assertIn("Currency: USD ($)", output)

    def test_collect_inputs_default_currency_argument_is_optional(self):
        with patch(
            "builtins.input",
            side_effect=[
                "28",  # age
                "n",  # retirement account?
                "n",  # property ownership?
                "1000",  # cash_and_bank
                "500",  # investments
                "100",  # other_assets
                "50",  # credit_card_debt
                "200",  # loans
                "0",  # other_liabilities
                "3000",  # monthly_income
                "2000",  # monthly_expenses
                "300",  # monthly_debt_payments
            ],
        ):
            sheet = pbs.collect_inputs()

        self.assertEqual(sheet.age, 28)
        self.assertEqual(sheet.retirement_accounts, 0.0)
        self.assertEqual(sheet.real_estate_value, 0.0)
        self.assertEqual(sheet.mortgage_balance, 0.0)


if __name__ == "__main__":
    unittest.main()
