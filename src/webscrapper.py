import cloudscraper
import pandas as pd

def scrapper(symbol):
    url = "https://www.nepsealpha.com/trading/1/history"
    params = {
        "fsk": "rpEzO8wdmCtGJiAY",
        "symbol": symbol, 
        "resolution": "1D",
        "pass": "ok"
    }
  
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url, params=params)
    response.raise_for_status()
    df = pd.DataFrame(response.json())
    #df.to_csv(f'../data/{symbol}.csv',index=False)
    return df

if __name__ =='__main__':
    df = scrapper("CLI")
    df.head(5)
    #df.to_csv('../data/Life_Insurance/CLI.csv',index=False)
    

