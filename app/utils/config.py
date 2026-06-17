from dotenv import load_dotenv
import os

load_dotenv()  # reads .env file and loads into environment

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")  # default value
APP_ENV = os.getenv("APP_ENV", "development")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing. Check your .env file.")