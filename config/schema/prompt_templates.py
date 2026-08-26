from langchain_core.prompts import PromptTemplate


top_news_prompt = PromptTemplate(
    template="""You are an expert financial journalist. Below is a list of financial news articles.

Select the 15 most important and relevant recent stories, prioritizing Indian markets, the economy, companies, policy developments, and market activity. Include major international stories when they have meaningful global market impact.

Rewrite each selected story clearly and concisely in your own words, around 200 words.

Return a structured list where every item contains:
- title: engaging headline
- article: concise rewritten article
- source: original source

News Articles:
{news_data}
""",
    input_variables=["news_data"],
)


top_insights_prompt = PromptTemplate(
    template="""You are a financial analyst and market strategist. Analyze the supplied financial news articles.

Extract up to 20 concise, evidence-based market insights that may affect stocks, indices, sectors, or commodities. Each insight should:
- Identify the impacted stock or sector.
- Explain the potential implication in 1-2 sentences.
- Classify sentiment as positive, negative, or neutral.
- Avoid unsupported claims and base the insight on the provided article content.

News Articles:
{news_data}
""",
    input_variables=["news_data"],
)
