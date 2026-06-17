from fastapi import FastAPI
import uvicorn

from app.models import AnalysisRequest, AnalysisResult, HealthCheck 
from app.services.analyzer import analyze_resume

app = FastAPI()

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
