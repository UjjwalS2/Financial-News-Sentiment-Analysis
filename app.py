from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from config.constants.constant import API_VERSION, SYMBOLS, URLS
from config.schema.prompt_templates import top_insights_prompt, top_news_prompt
from src.indices_data import indices_data
from src.models import insight_llm, news_llm
from src.news_collection import news_collector

load_dotenv()

app = FastAPI(
    title="AI-Powered Financial News and Insights API",
    version=API_VERSION,
    description="Get summarized financial news and market insights generated using Google Gemini.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", status_code=200)
def root():
    return {"message": "Welcome to the AI-powered Financial News Aggregator and Insights API."}


@app.get("/about", status_code=200)
def about():
    return {
        "message": "This API provides financial news summaries, AI-generated market insights, and market-index price data."
    }


@app.get("/health", status_code=200)
def health():
    return {"status": "OK", "version": API_VERSION}


@app.get("/get_top_news")
def get_top_news():
    news_data = news_collector(URLS)
    if not news_data:
        raise HTTPException(status_code=404, detail="Unable to fetch news data")
    try:
        response = (top_news_prompt | news_llm).invoke({"news_data": news_data}).top_news
        return response
    except Exception as exc:
        return JSONResponse(status_code=500, content={"message": f"An error occurred: {exc}"})


@app.get("/get_news_insight")
def get_news_insight():
    news_data = news_collector(URLS)
    if not news_data:
        raise HTTPException(status_code=404, detail="Unable to fetch news data")
    try:
        response = (top_insights_prompt | insight_llm).invoke({"news_data": news_data}).top_news
        return response
    except Exception as exc:
        return JSONResponse(status_code=500, content={"message": f"An error occurred: {exc}"})


@app.get("/indices_price_data")
def get_indices_price_data():
    price_data = indices_data(SYMBOLS)
    if not price_data:
        raise HTTPException(status_code=404, detail="Unable to fetch indices price data")
    return JSONResponse(status_code=200, content=price_data)
