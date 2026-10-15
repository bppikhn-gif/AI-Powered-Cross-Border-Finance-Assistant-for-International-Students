# AI-Powered-Cross-Border-Finance-Assistant-for-International-Students
My first repository on GitHub."
## Team
- Md. Bappi Pramanik (Team Leader), Ufa University of Science and Technology
- [Teammate 2] UUST RUSSIA
- [Teammate 3], City University Bangladesh

## What it does
- Compares transfer routes by fee, amount received and speed
- Builds a monthly budget from income and expenses
- Prepares a payment in a sandbox account
- Explains each recommendation in plain language

## Security design
- **Three permission tiers:** advice only, prepare payment, and execute payment
  only after the user types "yes".
- **Confirmation is enforced in code**, so the AI model cannot send a payment on its own.
- **Spending limit** of 2,000 USD per payment.
- **Audit log** of every message, tool call and result (`audit_log.jsonl`).
- No real card or account numbers are stored.

## How to run
1. Install Python 3.9 or newer.
2. Install the library: `pip install anthropic`
3. Set your API key:
   - Mac/Linux: `export ANTHROPIC_API_KEY=your_key`
   - Windows: `set ANTHROPIC_API_KEY=your_key`
4. Start the agent: `python agent.py`
5. Try: "I need to send 50,000 rubles to my family in Bangladesh. Which route is best?"

## Limitations
- Exchange rates and fees are sample data, labelled with a date.
- All payments run in a sandbox. No real money moves.
