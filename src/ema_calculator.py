import pandas as pd



def EMA_Calculator(df):
    """
    Calculate EMA on Daily Price 
    Calculate EMA on Weekly Price
    Window size is (5, 10, 15)
    """
    try:
        # Validate input
        if df is None or df.empty:
            raise ValueError("Empty DataFrame received")
            
        required_columns = {'datetime', 'price_1d'}
        if not required_columns.issubset(df.columns):
            missing = required_columns - set(df.columns)
            raise ValueError(f"Missing required columns: {missing}")

        # Convert to datetime and set as index
        df = df.copy()  # Avoid modifying original
        df['datetime'] = pd.to_datetime(df['datetime'])
        df = df.set_index('datetime').sort_index()
        
        # Daily EMAs
        for span in [5, 10, 15]:
            df[f'1D_EMA_{span}'] = df['price_1d'].ewm(span=span, adjust=False).mean()

        # Weekly resampling
        weekly_df = df['price_1d'].resample('W-THU').mean().to_frame('price_1w')
        
        # Weekly EMAs
        for span in [5, 10, 15]:
            weekly_df[f'1W_EMA_{span}'] = weekly_df['price_1w'].ewm(span=span, adjust=False).mean()
        
        # Merge weekly data
        df = df.join(weekly_df, how='left')
        
        # Reset index to make datetime a column again
        df = df.reset_index()
        df.tail()
        
        return df
        
    except Exception as e:
        print(f"❌ EMA Calculation Error: {str(e)}")
        return None