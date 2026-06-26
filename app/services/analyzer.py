import time
from app.models import AnalysisRequest, AnalysisResult
from app.utils.exceptions import AnalysisError, InvalidInputError
from app.services.llm import LLMService

MAX_RETRIES = 3

def analyze_resume(request: AnalysisRequest) -> AnalysisResult:
    """
    Analyzes a resume against a job description.
    Returns a structured AnalysisResult.
    Retries up to MAX_RETRIES times on transient failures.
    """
    last_error = None
    if not request.resume.strip():
        raise InvalidInputError("Resume cannot be empty")
    if not request.job_description.strip():
        raise InvalidInputError("Job description cannot be empty")
    if len(request.resume.strip()) < 50:
        raise InvalidInputError("Resume is too short to analyze meaningfully")

    llm = LLMService()
    for attempt in range(MAX_RETRIES):
        try:
           return llm.call_llm(request)

        except InvalidInputError as e:
            # Invalid input should not be retried
            raise 
        
        except Exception as e:
             # catches transient API errors — we'll replace with specific ones
             # when we wire up the real LLM next lesson
            wait = 2 ** attempt
            print(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait}s...")
            time.sleep(wait)
            last_error = e

    raise AnalysisError(f"Analysis failed after {MAX_RETRIES} attempts") from last_error