# Report — AppleSupport AI Support Agent

## Problem framing
Build an agent that (1) classifies incoming customer messages into a small set of data-derived intents, (2) drafts a reply grounded in historical AppleSupport resolutions, and (3) decides auto-handle vs human escalation with a reason.

Good means interpretable routing, traceable historical evidence, conservative escalation, and reproducible evaluation. We do not build live Twitter integration, autonomous account actions, production authentication, or policy guarantees.

## Data and system
AppleSupport was selected because the supplied TWCS data contains substantial AppleSupport activity. Incoming messages are paired to AppleSupport responses through TWCS response IDs. The classifier uses TF-IDF + logistic regression. Retrieval uses TF-IDF cosine similarity restricted to the predicted intent. Escalation triggers on high-risk/sensitive language or low intent confidence. The response exposes top historical evidence.

## Evaluation and baselines
The repo includes a 200-example golden-set draft and a majority-class trivial baseline. A transparent keyword rubric is used to seed labels. Because the same rubric creates training labels and draft gold labels, the current metric is not independent evidence. Before submission, manually verify the 200 labels and use a leakage-safe thread/time split with near-duplicate removal. Report final accuracy and macro-F1 only after this process.

## Failure analysis
1. Multi-issue tweets are forced into one intent.
2. Very short messages lack lexical signal.
3. Keyword collisions such as “charge” can confuse battery vs billing.
4. Historical replies may contain stale wording or links.
5. Single-turn context can omit the information needed to solve the case.

## What is misleading about my headline number?
A high score can be misleading because weak labels and training data share the same rubric, and Twitter contains repeated templates/near-duplicates. Random row splits can therefore overstate generalization. Human verification, thread-level/time splits and deduplication are required for a credible headline number.

## LLM judge
The judge scores groundedness, helpfulness, tone and safety from 1–5. To demonstrate judge agreement, humans should rate a 30–50 example subset and compare judge vs human scores (e.g. Spearman correlation and adjacent/exact agreement). Do not invent agreement numbers.

## One more week
Human-label the gold set; add conversation context; use embedding retrieval with freshness/policy filters; calibrate confidence; add adversarial tests; and add observability/policy checks.
