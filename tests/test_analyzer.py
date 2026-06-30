
import pytest

from app.models import AnalysisRequest, AnalysisResult
from app.services.analyzer import analyze_resume
from app.utils.exceptions import InvalidInputError
from unittest.mock import patch
from pydantic import ValidationError

def test_empty_resume_raises_error():
    with pytest.raises(InvalidInputError):
        analyze_resume(AnalysisRequest(
            resume="     " * 20,
            job_description="Looking for senior developer " * 3
        ))
      
def test_whitespace_job_description_raises_error():
    # Whitespace job description → caught by Pydantic → ValidationError
    with pytest.raises(ValidationError):
        AnalysisRequest(
            resume="Experienced Python developer " * 5,
            job_description=" " * 3
        )
def test_analyze_resume_returns_result():
    # Create a fake AnalysisResult to return
    fake_result = AnalysisResult(
        match_score=85,
        summary="Strong candidate with relevant experience",
        strengths=["Python", "FastAPI"],
        gaps=["Docker"],
        rewritten_summary="Experienced Python engineer"
    )

    # Replace LLMService.call_llm with a fake that returns fake_result
    with patch("app.services.analyzer.LLMService") as MockLLM:
        MockLLM.return_value.call_llm.return_value = fake_result
        
        result = analyze_resume(AnalysisRequest(
            resume="Experienced Python developer " * 5,
            job_description="Looking for senior Python developer " * 3
        ))
        
        assert result.match_score == 85
        assert "Python" in result.strengths