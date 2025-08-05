# Financial Indicator Sentiment Analysis

A comprehensive toolkit for analyzing and visualizing market sentiment for financial instruments using technical indicators, web scraping, and data science techniques.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Python API](#python-api)
- [Modules Overview](#modules-overview)
- [Data Sources](#data-sources)
- [Notebooks](#notebooks)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Market Sentiment Prediction:** Predicts bullish/bearish/neutral sentiment for stocks using EMA-based technical analysis.
- **Web Scraping:** Collects the latest stock data from online sources.
- **Data Preprocessing:** Cleans and prepares raw data for analysis.
- **Technical Indicator Calculation:** Computes EMAs and other indicators.
- **Extensible Data Handling:** Supports multiple data sources and categories.

---

## Project Structure

```
financial_indicator_sentiment/
│
├── main.py                        # Main logic for sentiment prediction
├── requirements.txt               # Python dependencies
├── Market Sentiment Feature Technical Documentation.pdf
│
├── src/                           # Source code modules
│   ├── data_preprocessing.py      # Data cleaning and preprocessing
│   ├── ema_calculator.py          # EMA calculation logic
│   └── webscrapper.py             # Web scraping utilities
│
├── data_from_api/                 # Example CSVs from APIs
│   ├── STC.csv
│   ├── CORBL.csv
│   └── ... (other stock CSVs)
│
├── notebooks/                     # Jupyter notebooks for exploration
│   ├── main.ipynb
│   ├── webscrapping.ipynb
│   └── closing_price_and_sma.png
```

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone 'https://github.com/cyrolux123/Intern-Ashad/tree/main/financial_indicator_sentiment'
   cd financial_indicator_sentiment
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Python API

You can use the sentiment prediction logic in your own scripts:
```python
from main import predict_sentiment

result = predict_sentiment("NABIL")
print(result)
```

---

## Modules Overview

- **main.py:** Orchestrates the sentiment prediction pipeline:
  1. Web scrapes data for a symbol.
  2. Preprocesses the data.
  3. Calculates EMAs.
  4. Computes bullish/bearish/neutral sentiment for intraday and weekly timeframes.

- **src/webscrapper.py:** Contains functions to fetch the latest stock data from web sources.

- **src/data_preprocessing.py:** Cleans and formats raw data for analysis.

- **src/ema_calculator.py:** Calculates Exponential Moving Averages (EMAs) for different periods.

---

## Data Sources

- **data_from_api/**: Contains sample CSVs for various stocks, used for testing and offline analysis.

---

## Notebooks

- **notebooks/main.ipynb:** End-to-end workflow demonstration.
- **notebooks/webscrapping.ipynb:** Web scraping experiments and data collection.
- **notebooks/closing_price_and_sma.png:** Visualization of closing prices and SMAs.

---

## Dependencies

Key dependencies (see `requirements.txt` for full list):

- `pandas`, `numpy` - Data manipulation
- `scikit-learn`, `scipy` - Data science utilities
- `ta`, `pandas-ta` - Technical analysis
- `requests`, `beautifulsoup4`, `selenium` - Web scraping
- `matplotlib`, `seaborn`, `plotly` - Visualization

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## Contributing

Contributions are welcome! Please open issues or pull requests for improvements, bug fixes, or new features.

---

## License

[MIT License](LICENSE) (or specify your license here)

---

**For more details, see the included technical documentation PDF.**