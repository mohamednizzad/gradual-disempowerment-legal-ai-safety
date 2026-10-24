# Metric definitions and interpretation

This document describes a transparent starter implementation. The metrics require validation before use in empirical research.

## 1. Text retention similarity

`text_retention_similarity(A, F)` computes TF-IDF cosine similarity between an AI-generated draft and a final draft.

\[
R_{\text{text}} = \cos(\mathrm{TFIDF}(A), \mathrm{TFIDF}(F))
\]

**Interpretation:** lexical and phrase overlap under this representation. A high score can mean appropriate adoption of correct material. It cannot, alone, measure deference, intent preservation, judgment, or agency.

## 2. Incorrect-claim retention rate

\[
D_{\text{incorrect}} =
\frac{\text{incorrect AI claims retained}}
{\text{incorrect AI claims presented}}
\]

This requires independent expert annotation of which claims are incorrect and whether they remain in the final output. Use `None` when the denominator is zero.

## 3. Seeded-error detection rate

\[
E_{\text{detect}} =
\frac{\text{seeded errors correctly detected}}
{\text{seeded errors presented}}
\]

The error set should be reviewed by qualified domain experts. Seeded errors should be realistic but safe and clearly controlled by the research protocol.

## 4. Evidence-horizon change

\[
\mathrm{EHC} = 1 - \frac{U_{\mathrm{AI}}}{U_{\mathrm{control}}}
\]

where \(U\) is the count of unique relevant authorities meeting a pre-defined quality threshold. Positive values indicate fewer qualifying authorities in the AI condition; negative values indicate more. Compare matched tasks only, and do not treat this measure as a direct harm indicator.

## Validation plan

- Define the annotation rubric before looking at condition-level results.
- Use two independent reviewers for a subset and report agreement.
- Measure citation correctness, relevance, and coverage, not counts alone.
- Compare the automated metrics against blinded expert ratings.
- Report missingness, uncertainty, sensitivity analyses, and negative results.
- Avoid individual rankings or performance claims from a small pilot.
