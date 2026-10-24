import pytest

from src.metrics import (
    evidence_horizon_change,
    incorrect_claim_retention_rate,
    safe_rate,
    seeded_error_detection_rate,
    text_retention_similarity,
)


def test_identical_text_has_similarity_one():
    text = "The fictional clause requires written notice."
    assert text_retention_similarity(text, text) == pytest.approx(1.0)


def test_empty_text_returns_zero():
    assert text_retention_similarity("", "Some draft") == 0.0


def test_safe_rate_zero_denominator():
    assert safe_rate(0, 0) is None


def test_incorrect_claim_retention_rate():
    assert incorrect_claim_retention_rate(1, 4) == pytest.approx(0.25)


def test_seeded_error_detection_rate():
    assert seeded_error_detection_rate(3, 4) == pytest.approx(0.75)


def test_evidence_horizon_change():
    assert evidence_horizon_change(4, 5) == pytest.approx(0.2)


def test_evidence_horizon_can_be_negative():
    assert evidence_horizon_change(6, 5) == pytest.approx(-0.2)


def test_evidence_horizon_zero_control_is_undefined():
    assert evidence_horizon_change(4, 0) is None
