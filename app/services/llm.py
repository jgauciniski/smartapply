from dataclasses import dataclass
from openai import OpenAI
from app.models import AnalysisRequest, AnalysisResult
from app.utils.config import MODEL_NAME, OPENAI_API_KEY
from app.utils.prompts import SYSTEM_PROMPT

@dataclass
class LLMService:
    """
    Service class to interact with the OpenAI API.
    """
    api_key: str = OPENAI_API_KEY
    model: str = MODEL_NAME
    system_prompt: str = SYSTEM_PROMPT

    def call_llm(self, prompt: AnalysisRequest) -> AnalysisResult:
        """
        Calls the LLM with the given prompt and returns the response.
        """
        client = OpenAI(api_key=self.api_key)
        response = client.beta.chat.completions.parse(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": f"RESUME:\n{prompt.resume}\n\nJOB DESCRIPTION:\n{prompt.job_description}"}
            ],
            max_tokens=1000,
            temperature=0.1,
            response_format=AnalysisResult
        )
        
        return response.choices[0].message.parsed