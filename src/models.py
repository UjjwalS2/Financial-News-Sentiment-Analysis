from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from config.schema.output_schema import NewsInsightResponse, TopNewsResponse

load_dotenv()

news_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.3)
insight_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.4)

news_llm = news_model.with_structured_output(TopNewsResponse)
insight_llm = insight_model.with_structured_output(NewsInsightResponse)
