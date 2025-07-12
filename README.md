# AI-Stock-Price-Prediction

## About the Project

This web application predicts future stock closing prices using historical data and a Long Short-Term Memory (LSTM) neural network. Users enter a stock symbol (e.g., AAPL), and the app fetches data from Yahoo Finance, trains an LSTM model on past closing prices, and displays:

* A plot of historical closing prices
* The predicted next closing price

This project demonstrates:

* Time-series forecasting with LSTM
* Data preprocessing (scaling, train-test split)
* Model training and evaluation
* Web integration using Flask for an interactive UI
* Plotting results with Matplotlib

## Features

* Input any valid stock ticker symbol
* Data fetching via the `yfinance` library
* Real-time model training and prediction
* Historical price chart display
* Clear, responsive HTML interface

## Folder Structure

```
stock_price_predictor/  
├── app.py            # Flask application and LSTM model code
├── requirements.txt  # Python dependencies
├── static/           # Folder for generated plot image (plot.png)
└── templates/        # HTML template
    └── index.html    # Frontend form and result display
```

## Prerequisites

* Python 3.7+
* pip (Python package installer)

## Installation & Setup

1. **Clone the repository**

   ```bash
   git clone <repository_url>
   cd stock_price_predictor
   ```
2. **Create & activate a virtual environment** (optional but recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate       # Windows
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## How to Run

1. **Ensure you are in the project root**

   ```bash
   cd stock_price_predictor
   ```
2. **Start the Flask app**

   ```bash
   python app.py
   ```
3. **Open your web browser** and navigate to `http://localhost:5000`
4. **Enter a stock symbol** (e.g., `AAPL`, `GOOG`, `TSLA`) and click **Predict**
5. **View the chart** and **predicted next closing price** on the page

## Notes

* The LSTM model is trained every time a prediction request is made; for large datasets or frequent use, consider saving and loading a pre-trained model.
* The date range for data fetching is hard-coded (2015–2024). Adjust `start` and `end` dates in `app.py` if needed.

## Future Enhancements

* Persist the trained model to disk and load it for faster predictions
* Add custom date-range input for users
* Improve UI/UX with Bootstrap or other CSS frameworks
* Deploy on a cloud platform (Heroku, AWS Elastic Beanstalk)
* Integrate additional technical indicators or sentiment analysis as input features

---

*Created by Sanjay, July 2025*
