# Data dictionary

The sample CSV contains fictional illustrative rows. It is not empirical participant data.

| Column | Meaning |
|---|---|
| `task_id` | Synthetic task identifier |
| `participant_id` | Synthetic participant identifier; use pseudonyms in approved research data |
| `condition` | Experimental condition, e.g. `ai_assisted` or `control` |
| `ai_draft` | AI draft text; blank for control tasks if not applicable |
| `final_draft` | Participant's final task output |
| `incorrect_claims_retained` | Expert-annotated count of incorrect AI claims retained |
| `incorrect_claims_presented` | Count of incorrect AI claims presented |
| `seeded_errors_detected` | Number of seeded errors correctly identified |
| `seeded_errors_presented` | Number of seeded errors presented |
| `unique_relevant_authorities` | Count of unique relevant authorities meeting the rubric threshold |
| `matched_control_authorities` | Comparable control-condition count used for the evidence-horizon calculation |

Before collecting real data, create a versioned protocol and specify allowed missing values, annotation rules, and task matching logic. Do not place names, client details, privileged information, or confidential documents in this dataset.
