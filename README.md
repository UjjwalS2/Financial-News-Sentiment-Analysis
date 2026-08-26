# Financial News Sentiment Analysis API

An AI-powered FastAPI service that collects recent financial news, rewrites and summarizes important stories with Google Gemini, extracts market insights with sentiment labels, and exposes live market-index data.

## Features

- 📰 Collect financial news from multiple RSS feeds
- ✍️ AI-rewrite and summarize the most relevant stories
- 📈 Generate stock/sector market insights from current headlines
- 🧠 Classify market sentiment as positive, negative, or neutral
- 📊 Return index and currency market data through Yahoo Finance
- ⚡ FastAPI REST endpoints with Swagger documentation
- 🐳 Docker-ready deployment

## Architecture

```text
RSS Financial News Sources
          ↓
   Feed Collection Layer
          ↓
 Article Extraction (newspaper3k)
          ↓
      Google Gemini
       ↙          ↘
 Top News      Market Insights
                + Sentiment
          ↓
      FastAPI JSON API

Yahoo Finance ───────→ Market Index Data
```

## Tech Stack

| Technology | Role |
|---|---|
| FastAPI | REST API framework |
| LangChain | LLM orchestration and prompt management |
| Google Gemini 2.0 Flash | News summarization and market insight generation |
| Pydantic | Structured LLM output validation |
| feedparser | RSS feed ingestion |
| newspaper3k | Article content extraction |
| yfinance | Market/index data |
| Uvicorn | ASGI server |
| Docker | Containerized deployment |

## API Endpoints

### `GET /`
Returns the service welcome message.

### `GET /about`
Describes the service capabilities.

### `GET /health`
Returns health status and API version.

### `GET /get_top_news`
Collects recent financial articles and uses Gemini to return the most relevant stories in a structured format.

### `GET /get_news_insight`
Analyzes collected financial news and returns concise stock/sector insights with sentiment labels.

### `GET /indices_price_data`
Returns market data for configured indices and USD/INR using Yahoo Finance symbols.

## Setup

### 1. Clone

```bash
git clone https://github.com/UjjwalS2/Financial-News-Sentiment-Analysis.git
cd Financial-News-Sentiment-Analysis
```

### 2. Create environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini

Copy `.env.example` to `.env` and add a valid Google Gemini API key:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

### 5. Run

```bash
uvicorn app:app --reload
```

Interactive Swagger docs:

`http://127.0.0.1:8000/docs`

## Docker

```bash
docker build -t financial-news-sentiment-api .
docker run --env-file .env -p 8000:8000 financial-news-sentiment-api
```

## Project Structure

```text
Financial-News-Sentiment-Analysis/
├── app.py
├── config/
│   ├── __init__.py
│   ├── constants/
│   │   ├── __init__.py
│   │   └── constant.py
│   └── schema/
│       ├── __init__.py
│       ├── output_schema.py
│       └── prompt_templates.py
├── src/
│   ├── __init__.py
│   ├── indices_data.py
│   ├── models.py
│   └── news_collection.py
├── .env.example
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
```

## Data Sources

The application is configured to ingest financial RSS feeds from sources such as Economic Times, Business Standard, Livemint, and CNBC. Market data is retrieved through Yahoo Finance symbols configured in `config/constants/constant.py`.

## Important Note

This project is intended for educational and engineering demonstration purposes. AI-generated insights are not investment advice, and market data/news availability depends on the upstream providers.

## Author

**Ujjwal Sinha**

GitHub: https://github.com/UjjwalS2
