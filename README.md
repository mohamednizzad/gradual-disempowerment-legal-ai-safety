# Measuring Gradual Disempowerment in AI-Assisted Legal Reasoning

> **Research prototype.** This repository is a starter kit for a proposed technical AI Safety pilot. It contains synthetic example data and illustrative metrics. It is not a validated diagnostic for human agency, legal competence, or AI safety.

## Research objective

Explore whether observable task-level signals can help identify patterns that may warrant further investigation in AI-assisted legal research and drafting. The prototype combines text-retention measures, seeded-error detection, and citation/evidence metrics. No single metric is treated as proof of disempowerment.

## Research questions

1. Does AI assistance change the extent to which legal professionals retain, revise, or reject model-generated text?
2. Does AI assistance change the breadth, relevance, and correctness of authorities used?
3. Is retention of incorrect AI claims associated with lower detection of seeded errors?

## Repository contents

```text
.
├── README.md
├── LICENSE
├── CITATION.cff
├── pyproject.toml
├── requirements.txt
├── .gitignore
├── data/
│   └── sample/
│       └── synthetic_tasks.csv
├── docs/
│   ├── DATA_DICTIONARY.md
│   ├── ETHICS_AND_PRIVACY.md
│   └── METRICS.md
├── src/
│   └── metrics.py
└── tests/
    └── test_metrics.py
```

## Quick start

Python 3.10+ is recommended.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
pytest
python -m src.metrics --input data/sample/synthetic_tasks.csv --output results.csv
```

The command writes a task-level metric table to `results.csv`. It does not send data to an external service.

## Prototype metrics

- **Text retention similarity:** cosine similarity between TF-IDF representations of an AI draft and a final draft. This is a lightweight baseline, not a semantic or agency measure.
- **Incorrect-claim retention rate:** incorrect claims retained divided by incorrect claims presented, where those counts have been independently annotated.
- **Seeded-error detection rate:** seeded errors correctly identified divided by seeded errors presented.
- **Evidence-horizon comparison:** relative change in unique relevant authorities between matched AI-assisted and control tasks. Use only when tasks are matched and the control count is non-zero.

Metric definitions and caveats are in [`docs/METRICS.md`](docs/METRICS.md).

## Important interpretation safeguards

1. High text similarity can reflect appropriate adoption of correct material. It does not prove rubber-stamping.
2. Low similarity can reflect stylistic editing rather than better reasoning.
3. Citation counts are not a substitute for citation relevance, correctness, or coverage.
4. A pilot with a small sample should emphasize effect sizes, uncertainty, and descriptive results.
5. Do not collect privileged, confidential, or identifiable client material. Use fictionalized, public-domain, or ethics-approved tasks.
6. Do not publish participant-level records. Public data should be synthetic or reviewed and approved for release.

## Data status

`data/sample/synthetic_tasks.csv` contains fictional illustrative rows only. It is not real participant data and must not be described as empirical findings.

## Suggested next research steps

- Pre-register the protocol and primary outcomes before collection.
- Develop matched legal tasks with expert-reviewed answer rubrics.
- Have at least two reviewers independently annotate a subset and report agreement.
- Evaluate metric reliability against blinded human ratings.
- Compare alternative text representations and perform sensitivity analysis.
- Publish negative and inconclusive results alongside positive findings.

## License

MIT for the code and documentation in this repository. Any future participant data or third-party materials may require separate terms and must not automatically be assumed to fall under this license.
