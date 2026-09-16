# Decision Log
1. AppleSupport selected for sufficient support volume.
2. Brand-isolated data prevents cross-brand response leakage.
3. Ten intents balance coverage and interpretability.
4. TF-IDF + logistic regression keeps the prototype lightweight.
5. Retrieval is restricted to predicted intent.
6. Historical responses provide grounding evidence.
7. Confidence < 0.55 escalates.
8. Fraud/legal/threat/sensitive-data language escalates.
9. Top-3 evidence makes outputs auditable.
10. No autonomous account actions are allowed.
11. Golden set has 200 examples, within the requested range.
12. Gold labels are explicitly marked for human verification.
13. Majority class is the trivial baseline.
14. LLM judge is optional so core pipeline runs without API access.
15. Production integrations and policy guarantees are intentionally out of scope.
