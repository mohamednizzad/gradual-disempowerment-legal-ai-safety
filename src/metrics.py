"""Illustrative task-level metrics for a legal AI safety pilot.

All metrics are exploratory. None is a direct measurement of human agency.
This module uses TF-IDF cosine similarity as a transparent baseline.
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def text_retention_similarity(ai_draft: Optional[str], final_draft: Optional[str]) -> float:
    """Return TF-IDF cosine similarity in [0, 1]; 0 for empty inputs.

    High similarity means textual overlap in this representation. It does not
    establish whether adoption was justified or whether agency was reduced.
    """
    a = (ai_draft or "").strip()
    b = (final_draft or "").strip()
    if not a or not b:
        return 0.0
    matrix = TfidfVectorizer(ngram_range=(1, 2), lowercase=True).fit_transform([a, b])
    return float(cosine_similarity(matrix[0:1], matrix[1:2])[0, 0])


def safe_rate(numerator: float, denominator: float) -> Optional[float]:
    """Return numerator/denominator, or None when denominator is zero."""
    if denominator == 0:
        return None
    return float(numerator) / float(denominator)


def incorrect_claim_retention_rate(
    incorrect_claims_retained: float, incorrect_claims_presented: float
) -> Optional[float]:
    """Share of annotated incorrect AI claims retained in the final output."""
    return safe_rate(incorrect_claims_retained, incorrect_claims_presented)


def seeded_error_detection_rate(
    seeded_errors_detected: float, seeded_errors_presented: float
) -> Optional[float]:
    """Share of seeded errors correctly identified by the participant."""
    return safe_rate(seeded_errors_detected, seeded_errors_presented)


def evidence_horizon_change(
    ai_unique_relevant_authorities: float, control_unique_relevant_authorities: float
) -> Optional[float]:
    """Relative reduction in unique relevant authorities for an AI task vs control.

    Returns 1 - AI/control. Negative values mean the AI condition used more
    authorities. This is meaningful only for matched tasks and a non-zero
    control count; it is not itself evidence of harm.
    """
    if control_unique_relevant_authorities == 0:
        return None
    return 1.0 - (
        float(ai_unique_relevant_authorities) / float(control_unique_relevant_authorities)
    )


def analyze_csv(input_path: Path) -> pd.DataFrame:
    """Load task-level CSV and compute available prototype metrics."""
    df = pd.read_csv(input_path)

    required = {
        "task_id",
        "condition",
        "ai_draft",
        "final_draft",
        "incorrect_claims_retained",
        "incorrect_claims_presented",
        "seeded_errors_detected",
        "seeded_errors_presented",
        "unique_relevant_authorities",
        "matched_control_authorities",
    }
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")

    df["text_retention_similarity"] = df.apply(
        lambda row: text_retention_similarity(row["ai_draft"], row["final_draft"]),
        axis=1,
    )
    df["incorrect_claim_retention_rate"] = df.apply(
        lambda row: incorrect_claim_retention_rate(
            row["incorrect_claims_retained"], row["incorrect_claims_presented"]
        ),
        axis=1,
    )
    df["seeded_error_detection_rate"] = df.apply(
        lambda row: seeded_error_detection_rate(
            row["seeded_errors_detected"], row["seeded_errors_presented"]
        ),
        axis=1,
    )
    df["evidence_horizon_change"] = df.apply(
        lambda row: evidence_horizon_change(
            row["unique_relevant_authorities"], row["matched_control_authorities"]
        ),
        axis=1,
    )
    return df


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="Input CSV path")
    parser.add_argument("--output", required=True, type=Path, help="Output CSV path")
    args = parser.parse_args()

    result = analyze_csv(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(args.output, index=False)
    print(f"Wrote {len(result)} task rows to {args.output}")
    print("Reminder: metrics are exploratory and do not establish disempowerment.")


if __name__ == "__main__":
    main()
