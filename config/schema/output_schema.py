from typing import List
from pydantic import BaseModel, Field


class NewsItem(BaseModel):
    title: str = Field(description="Title of the news article")
    article: str = Field(description="AI-rewritten article")
    source: str = Field(description="News source")


class TopNewsResponse(BaseModel):
    top_news: List[NewsItem] = Field(description="Relevant recent financial news articles")


class NewsInsight(BaseModel):
    stock_or_sector: str = Field(description="Impacted stock or sector")
    insight: str = Field(description="Concise market insight")
    sentiment: str = Field(description="Positive, negative, or neutral")


class NewsInsightResponse(BaseModel):
    top_news: List[NewsInsight] = Field(description="Financial market insights")
