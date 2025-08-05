import pandas as pd
from src.webscrapper import scrapper
from src.data_preprocessing import data_preprocess
from src.ema_calculator import EMA_Calculator

def predict_sentiment(symbol):
    """
    Performs sentiment analysis for a given symbol by:
    1. Web scraping latest data
    2. Preprocessing the data
    3. Calculating EMAs
    4. Determining market sentiment for both intraday and weekly timeframes
    
    Args:
        symbol (str): Stock symbol to analyze
        
    Returns:
        dict: Analysis results with keys:
            - 'symbol'
            - 'intraday_score'
            - 'weekly_score'
            - 'intraday_trend'
            - 'weekly_trend'
            - 'overall_signal'
            - 'error' (if any)
    """
    try:
        # Step 1: Get data
        stock_data = scrapper(symbol)
        if stock_data is None or stock_data.empty:
            raise ValueError("No data returned from scraper")
        
        # Step 2: Clean data
        cleaned_df = data_preprocess(stock_data)
        if cleaned_df is None or cleaned_df.empty:
            raise ValueError("Data preprocessing failed")
        
        # Step 3: Calculate EMAs
        symbol_data = EMA_Calculator(cleaned_df)
        if symbol_data is None or symbol_data.empty:
            raise ValueError("EMA calculation failed")
        
        # Validate required columns exist
        required_cols = ['price_1w', '1W_EMA_5', '1W_EMA_10', '1W_EMA_15', 
                        'price_1d', '1D_EMA_5', '1D_EMA_10', '1D_EMA_15']
        missing_cols = [col for col in required_cols if col not in symbol_data.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
        
        # Additional validation for data availability
        for col in required_cols:
            if symbol_data[col].dropna().empty:
                raise ValueError(f"No valid data for {col}")
            

        symbol_data.to_csv(f'./data_from_api/{symbol}.csv',index = False)
        
        # Step 4: Get most recent valid prices
        weekly_prices = symbol_data['price_1w'].dropna()
        if weekly_prices.empty:
            raise ValueError("No valid weekly prices available")
        price_1w = weekly_prices.iloc[-1]
        price_1d = symbol_data['price_1d'].iloc[-1]

        # Weekly Time Frame (1W) Analysis - Bullish vs Bearish Logic
        weekly_bullish_conditions = [
            price_1w > symbol_data['1W_EMA_5'].iloc[-1],
            symbol_data['1W_EMA_5'].iloc[-1] > symbol_data['1W_EMA_10'].iloc[-1],
            symbol_data['1W_EMA_10'].iloc[-1] > symbol_data['1W_EMA_15'].iloc[-1]
        ]
        
        weekly_bearish_conditions = [
            price_1w < symbol_data['1W_EMA_5'].iloc[-1],
            symbol_data['1W_EMA_5'].iloc[-1] < symbol_data['1W_EMA_10'].iloc[-1],
            symbol_data['1W_EMA_10'].iloc[-1] < symbol_data['1W_EMA_15'].iloc[-1]
        ]
        
        # Calculate weekly bullish and bearish counts
        weekly_bullish_count = sum(weekly_bullish_conditions)
        weekly_bearish_count = sum(weekly_bearish_conditions)
        total_weekly_signals = weekly_bullish_count + weekly_bearish_count
        
        # Calculate weekly bullish percentage (out of total signals)
        if total_weekly_signals > 0:
            weekly_score = (weekly_bullish_count / total_weekly_signals) * 100
        else:
            weekly_score = 50  # Neutral if no clear signals

        # Intraday Time Frame (1D) Analysis - Bullish vs Bearish Logic
        intraday_bullish_conditions = [
            price_1d > symbol_data['1D_EMA_5'].iloc[-1],
            symbol_data['1D_EMA_5'].iloc[-1] > symbol_data['1D_EMA_10'].iloc[-1],
            symbol_data['1D_EMA_10'].iloc[-1] > symbol_data['1D_EMA_15'].iloc[-1]
        ]
        
        intraday_bearish_conditions = [
            price_1d < symbol_data['1D_EMA_5'].iloc[-1],
            symbol_data['1D_EMA_5'].iloc[-1] < symbol_data['1D_EMA_10'].iloc[-1],
            symbol_data['1D_EMA_10'].iloc[-1] < symbol_data['1D_EMA_15'].iloc[-1]
        ]
        
        # Calculate intraday bullish and bearish counts
        intraday_bullish_count = sum(intraday_bullish_conditions)
        intraday_bearish_count = sum(intraday_bearish_conditions)
        total_intraday_signals = intraday_bullish_count + intraday_bearish_count
        
        # Calculate intraday bullish percentage (out of total signals)
        if total_intraday_signals > 0:
            intraday_score = (intraday_bullish_count / total_intraday_signals) * 100
        else:
            intraday_score = 50  # Neutral if no clear signals
        
        return {
            'symbol': symbol,
            'intraday_bullish': round(intraday_score, 2),
            'weekly_bullish': round(weekly_score, 2)
        }
        
    except Exception as e:
        return {
            'symbol': symbol,
            'intraday_bullish': 0,
            'weekly_bullish': 0,
            'error': str(e)
        }

if __name__ == "__main__":
    print('Sentiment Analysis has started..... :)')
    results = {}
    sentiment = predict_sentiment("MERO")
    
    # Updated results structure to handle new output format
    results = {
        "symbol": sentiment.get("symbol", ""),
        "intraday": int(round(sentiment.get("intraday_bullish", 0))),
        "weekly": int(round(sentiment.get("weekly_bullish", 0)))
    }
    
    print(results)
    
    if 'error' in sentiment:
        print(f"Error: {sentiment['error']}")

    print('\nSentiment Analysis has Finished..... :)')