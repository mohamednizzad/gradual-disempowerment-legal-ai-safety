# Measuring Gradual Disempowerment in AI-Assisted Legal Reasoning

**An exploratory technical AI Safety research prototype**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/tests-11%20passing-brightgreen)](#testing)
[![Status](https://img.shields.io/badge/status-exploratory%20prototype-orange)](#limitations)

## Overview

This project investigates how to measure potential changes in independent judgment, verification behaviour, and evidence-seeking when professionals use AI-assisted legal reasoning tools.

The central research question is whether repeated reliance on AI may be associated with observable changes in human oversight and the ability to reason independently.

The project does not assume that AI assistance necessarily causes disempowerment. It aims to develop a transparent, reproducible evaluation framework for investigating this possibility.

## Research Questions

1. How much of an AI-generated legal draft is retained in the final output?
2. How frequently are incorrect claims from AI-generated drafts retained?
3. How effectively do participants identify deliberately seeded errors?
4. Does the range of relevant legal authorities consulted differ between AI-assisted and unaided tasks?
5. Where repeated-session data are feasible, do verification behaviour or subsequent unaided performance change over time?

## Implemented Metrics

The current Python prototype implements the following exploratory measures:

| Metric | Purpose |
|---|---|
| Text retention similarity | Measures textual overlap between AI-generated and final drafts using TF-IDF cosine similarity. |
| Incorrect-claim retention rate | Measures the proportion of annotated incorrect claims retained in the final output. |
| Seeded-error detection rate | Measures the proportion of predefined errors correctly identified. |
| Evidence-horizon change | Measures the relative difference in unique relevant authorities between an AI task and its matched control. |

The prototype also includes basic input validation for rate calculations and automated tests for the implemented functions.

These metrics measure observable task-level indicators. None is a direct or independently validated measure of human agency.

## Repository Structure

```text
.
├── data/
│   └── sample/
│       └── synthetic_tasks.csv
├── docs/
│   ├── DATA_DICTIONARY.md
│   ├── ETHICS_AND_PRIVACY.md
│   └── METRICS.md
├── src/
│   └── metrics.py
├── tests/
│   └── test_metrics.py
├── CITATION.cff
├── LICENSE
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Getting Started

Python 3.10 or later is required.

### 1. Install dependencies

```bash
python -m pip install -r requirements.txt
python -m pip install pytest
```

### 2. Run the automated tests

```bash
python -m pytest -v
```

The current local test suite contains 11 tests covering basic metric behaviour and selected input-validation cases.

### 3. Run the sample analysis

```bash
python -m src.metrics --input data/sample/synthetic_tasks.csv --output data/sample/metrics_output.csv
```

The output file contains the calculated metrics for the supplied sample tasks.

## Sample Data

The included sample dataset contains three synthetic task records intended to demonstrate the analysis pipeline.

**These records are fictional and are not observations from real legal professionals.** They must not be interpreted as empirical evidence that AI improves or degrades legal reasoning.

## Planned Research

Subject to funding, recruitment feasibility, and applicable ethical approval, the proposed four-month pilot will:

1. Refine metric definitions and annotation procedures.
2. Conduct controlled AI-assisted and unaided legal reasoning tasks.
3. Examine error detection, independent verification, and evidence-seeking.
4. Explore repeated-session effects where feasible.
5. Publish a technical report and reusable research artefacts, subject to privacy and consent constraints.

## Limitations

- Textual similarity does not establish overreliance or loss of independent judgment.
- Error-detection rates depend on the quality of the predefined error key and annotation.
- Authority counts do not, by themselves, measure the quality of legal research.
- The current synthetic dataset is too small to support substantive empirical conclusions.
- The present prototype does not establish causal effects or validate a general measure of gradual disempowerment.

The project will report uncertainty and alternative explanations rather than interpret any single metric as proof of harm.

## Ethics and Privacy

The planned pilot will use fictional legal scenarios and controlled source materials rather than confidential client matters. Participant data will be handled according to the approved research protocol, consent arrangements, and applicable privacy requirements.

Participant recruitment and data collection will begin only after any required ethical review or approval.

## Funding Proposal

To be confirmed.

## License

See the repository's `LICENSE` file for licensing terms.

## Citation

Citation metadata is provided in `CITATION.cff`. Please cite the project using the repository's current metadata.

## Research Status

**Status:** Exploratory prototype. Empirical validation is pending.

The objective is to make potential changes in human oversight and independent reasoning more measurable and open to scientific scrutiny, not to presume that disempowerment has already occurred.