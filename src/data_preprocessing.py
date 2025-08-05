import pandas as pd


def data_preprocess(df):
    """
    Takes the raw dataframe
    Performs preprocessing and cleaning
    
    Args:
        df: Raw DataFrame with columns including 'c' (close price) and 't' (timestamp)
    
    Returns:
        Cleaned DataFrame with datetime column and price_1d column
        None if processing fails
    """
    try:
        # Validate input
        if df is None or df.empty:
            raise ValueError("Empty DataFrame received")
            
        required_columns = {'c', 't'}
        if not required_columns.issubset(df.columns):
            missing = required_columns - set(df.columns)
            raise ValueError(f"Missing required columns: {missing}")

        # Rename columns
        df = df.rename(columns={'c': 'price_1d', 't': 'datetime','h':'higest_price','l':'lowest_price','v':'volume','o':'open_price'})
        
        # Drop unnecessary columns if they exist
        cols_to_drop = ['s']
        df.drop(columns=[col for col in cols_to_drop if col in df.columns], inplace=True, errors='ignore')

        # Convert and validate datetime
        df['datetime'] = pd.to_datetime(df['datetime'], unit='s', errors='coerce')
        if df['datetime'].isnull().any():
            raise ValueError("Invalid timestamp values found")
            
        # Sort by datetime but keep as column
        df = df.sort_values('datetime')
        
        # Validate output
        if df.empty:
            raise ValueError("Processing resulted in empty DataFrame")
            
        return df
    
    except Exception as e:
        print(f'❌ Error in data preprocessing: {e}')
        return None