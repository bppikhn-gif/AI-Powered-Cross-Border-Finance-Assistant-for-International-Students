"""
StudentFin AI - offline demo (NO language model, NO API key, NO cost).

This script calls the same tools and security controls as agent.py, in the order
a real conversation would use them, and writes audit_log.jsonl.
It does NOT test the language model. It shows the tools, the permission tiers,
the spending limit and the human confirmation step.

Run:  py demo_offline.py
Save the console output:  py demo_offline.py > demo_output.txt
"""
import builtins
import json

import agent


def show(title, result):
    print(f"\n=== {title} ===")
    print(json.dumps(result, indent=2, ensure_ascii=False))


def scripted_answers(*answers):
    """Replace the human's keyboard input with fixed answers for this demo."""
    queue = list(answers)

    def fake_input(prompt=""):
        answer = queue.pop(0)
        print(f"{prompt}{answer}   <- scripted human answer")
        return answer

    builtins.input = fake_input


print("StudentFin AI offline demo (sample data, sandbox payments, no language model)")

# Tier 0: advice tools
show("1. Compare transfer routes: 50,000 RUB to BDT",
     agent.run_tool("compare_transfer_routes",
                    {"amount": 50000, "from_currency": "RUB", "to_currency": "BDT"}))
show("2. Study cost in Germany, 50% tuition scholarship, 200 USD stipend",
     agent.run_tool("estimate_study_costs",
                    {"country": "Germany", "months": 12,
                     "scholarship_tuition_percent": 50, "monthly_stipend_usd": 200}))
show("3. Forecast: 1000 USD, income 300, expenses 700 per month",
     agent.run_tool("forecast_budget",
                    {"starting_balance": 1000, "monthly_income": 300,
                     "monthly_expenses": 700, "currency": "USD", "months": 6}))
show("4. Same forecast with 150 USD part-time income",
     agent.run_tool("forecast_budget",
                    {"starting_balance": 1000, "monthly_income": 300,
                     "monthly_expenses": 700, "currency": "USD", "months": 6,
                     "part_time_income": 150}))

# Tier 1: prepare. The spending limit blocks a large payment.
show("5. Prepare a payment over the limit (900,000 RUB): must be refused",
     agent.run_tool("prepare_payment",
                    {"amount": 900000, "currency": "RUB",
                     "recipient": "University", "route": "Bank wire"}))

pending = agent.run_tool("prepare_payment",
                         {"amount": 30000, "currency": "RUB",
                          "recipient": "University", "route": "Money transfer app"})
show("6. Prepare a payment of 30,000 RUB: PENDING, nothing is sent", pending)
payment_id = pending["payment_id"]

# Tier 2: execute needs the human. First the human says no, then yes.
scripted_answers("no")
show("7. Execute: the human answers 'no'",
     agent.run_tool("execute_payment", {"payment_id": payment_id}))

scripted_answers("yes")
show("8. Execute again: the human answers 'yes' (sandbox payment)",
     agent.run_tool("execute_payment", {"payment_id": payment_id}))

show("9. Execute the same payment a second time: must fail",
     agent.run_tool("execute_payment", {"payment_id": payment_id}))

print(f"\nDone. Every step was written to {agent.AUDIT_FILE}.")
