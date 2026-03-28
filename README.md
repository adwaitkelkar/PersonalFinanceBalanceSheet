# Personal Finance Balance Sheet Tool (Python)

This project is a **simple Python tool** to create a personal balance sheet (similar to a company balance sheet, but easier) and calculate your **free cash flow**.
It uses **Euro (EUR)** by default and also lets you choose other currencies.
It is primarily designed for **young adults (ages 22-35)**.

## What this tool does

- Collects your personal finance numbers through an easy command-line prompt.
- Asks age first and is optimized for ages 22-35.
- Treats retirement accounts and property as optional (defaults to not included unless you confirm).
- Shows your:
  - Total Assets
  - Total Liabilities
  - Net Worth
  - Monthly Free Cash Flow
  - Yearly Free Cash Flow

---

## Balance sheet terms (simple explanations)

### Assets
Things you own that have value.

- **Cash + bank accounts**: Money you currently have in checking/savings.
- **Investments**: Stocks, ETFs, mutual funds, brokerage account value, etc.
- **Retirement accounts**: 401(k), IRA, pension account value, etc.
- **Real estate**: Current market value of your home or property.
- **Other assets**: Valuable items not listed above (for example, business ownership value or other major valuables).

### Liabilities
Money you owe.

- **Credit card debt**: Total unpaid credit card balance.
- **Loans**: Student loans, auto loans, personal loans.
- **Mortgage balance**: Remaining home loan amount.
- **Other liabilities**: Any other debts not listed above.

### Key outputs

- **Total Assets**: Sum of all assets.
- **Total Liabilities**: Sum of all liabilities.
- **Net Worth**: `Total Assets - Total Liabilities`.
  - Positive net worth means you own more than you owe.
  - Negative net worth means you owe more than you own.

### Free cash flow
Free cash flow means how much cash you have left after essential spending.

In this tool:

`Monthly Free Cash Flow = Monthly Income - Monthly Living Expenses - Monthly Debt Payments`

`Yearly Free Cash Flow = Monthly Free Cash Flow * 12`

If free cash flow is positive, you are generating extra cash each month. If negative, your monthly outflow is higher than inflow.

---

## Setup

### 1) Requirements

- Python 3.9+ (or newer)

### 2) Run the script

From this project folder:

```bash
python3 personal_balance_sheet.py
```

Then enter your values when prompted.

By default, the script formats all amounts in **Euro (EUR)**.

To choose another currency, use:

```bash
python3 personal_balance_sheet.py --currency USD
```

Supported currency codes:

- `EUR` (default)
- `USD`
- `GBP`
- `INR`
- `JPY`
- `CAD`
- `AUD`

---

## Quick demo mode (optional)

If you want to see sample output quickly:

```bash
python3 personal_balance_sheet.py --quick-example
```

You can combine quick demo mode with a currency selection:

```bash
python3 personal_balance_sheet.py --quick-example --currency EUR
```

---

## Example usage flow

1. Run the script.
2. Enter your age.
3. Confirm whether you have retirement accounts and/or own property.
4. Enter all requested amounts.
5. Read the printed report:
   - Assets section
   - Liabilities section
   - Net Worth
   - Free Cash Flow (monthly and yearly)

---

## Notes

- Enter values in your selected currency.
- Do not use negative numbers.
- You can rerun the script anytime to track progress monthly.
