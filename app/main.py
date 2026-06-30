from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

from app.models import AnalysisRequest, AnalysisResult, HealthCheck 
from app.services.analyzer import analyze_resume
from app.utils.exceptions import AnalysisError, InvalidInputError

app = FastAPI(title="SmartApply API", version="1.0.0", description="API for analyzing resumes against job descriptions using LLMs")

@app.exception_handler(InvalidInputError)
async def handle_invalid_input_error(request: Request, exc: InvalidInputError):
    return JSONResponse(status_code=422, content={"detail": str(exc)})

@app.exception_handler(AnalysisError)
async def handle_analysis_error(request: Request, exc: AnalysisError):
    return JSONResponse(status_code=500, content={"detail": str(exc)})

@app.get("/health", response_model=HealthCheck)
def get_health():
    return HealthCheck()

@app.post("/analyze", response_model=AnalysisResult)
def analyze(analysis_request: AnalysisRequest) -> AnalysisResult:
    return analyze_resume(analysis_request)

def main():
    print("starting the server...")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()
