from openai import OpenAI
# from app.core.config import OPENAI_API_KEY, OPENAI_BASE_URL, MODEL_NAME
from app.core.config import settings

client = OpenAI(
    api_key=settings.OPENAI_API_KEY,
    base_url=settings.OPENAI_BASE_URL
)