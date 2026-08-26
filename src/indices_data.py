import yfinance as yf


def indices_data(symbols: dict) -> dict:
    """Fetch current market-index data for the requested Yahoo Finance symbols."""
    data = {}
    for name, symbol in symbols.items():
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info
            price = info.get("regularMarketPrice")
            change = info.get("regularMarketChange")
            percent = info.get("regularMarketChangePercent")
            if price is None:
                continue
            data[name] = {
                "symbol": symbol,
                "price": round(price, 2),
                "change": round(change or 0, 2),
                "percent_change": round(percent or 0, 2),
            }
        except Exception:
            continue
    return data
