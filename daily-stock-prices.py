import yfinance as yf  
yf.download("AAPL", period="1d").to_csv("aapl_today.csv")
