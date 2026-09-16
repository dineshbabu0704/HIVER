# Hiver SDE Intern Take-Home — AppleSupport AI Support Agent

## Quick start
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python src/train.py
cd evaluation && python evaluate.py && cd ..
python run_agent.py "My iPhone battery is draining very quickly after the update"
```

The agent classifies an incoming message, retrieves historically similar AppleSupport cases, drafts a grounded reply, and decides auto-handle vs human escalation.

## Intents
battery, ios_update, app_crash_performance, connectivity, account_authentication, device_hardware, notifications_messages, media_music, purchase_billing, general_support.

## Evaluation
`evaluation/golden_set.csv` contains 200 pre-labeled examples. **The assignment requires hand-labelled examples, so you must personally review/correct these before submission.** The current metrics are intentionally not presented as final proof because training and draft gold labels share the same rubric.

The optional `evaluation/judge.py` uses an OpenAI model to score groundedness/helpfulness/tone/safety. Rate a human subset with `human_judge_template.csv` and compute agreement before claiming judge reliability.

## Scope
No live Twitter sending, account changes, production authentication, or guarantee of current Apple policies.
