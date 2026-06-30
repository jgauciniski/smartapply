from pydantic import ValidationError
import pytest
from app.models import AnalysisRequest, AnalysisResult

def test_valid_analysis_request():
    request = AnalysisRequest(
        resume="Experienced Python developer " * 5,
        job_description="Looking for senior Python developer " * 3
    )
    assert request.resume is not None  # ← assert is how you verify in pytest`
    assert request.job_description is not None

def test_match_score_above_100_fails():
    with pytest.raises(ValidationError):
        AnalysisResult(
            match_score=150,
            summary="Strong candidate",
            strengths=["Python"],
            gaps=["Docker"],
            rewritten_summary="Experienced engineer"
        )

def test_match_score_below_0_fails():
    with pytest.raises(ValidationError):
        AnalysisResult(
            match_score=-1,
            summary="Strong candidate",
            strengths=["Python"],
            gaps=["Docker"],
            rewritten_summary="Experienced engineer"
        )