# Stock Price Prediction Web App (Flask + LSTM)
# Backend: Flask with Keras LSTM Model
# Frontend: HTML form to input stock symbol and plot prediction

# Required Libraries:
# pip install flask pandas yfinance scikit-learn matplotlib tensorflow

from flask import Flask, request, render_template
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
import os

app = Flask(__name__)

# Create directory for storing plots if not exist
if not os.path.exists("static"):
    os.makedirs("static")


def create_model(train_data, time_step=60):
    x, y = [], []
    for i in range(time_step, len(train_data)):
        x.append(train_data[i - time_step:i, 0])
        y.append(train_data[i, 0])
    x, y = np.array(x), np.array(y)
    x = x.reshape((x.shape[0], x.shape[1], 1))

    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(x.shape[1], 1)))
    model.add(LSTM(50))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x, y, epochs=5, batch_size=32, verbose=0)
    return model


@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    plot_url = None

    if request.method == 'POST':
        symbol = request.form['symbol'].upper()
        df = yf.download(symbol, start='2015-01-01', end='2024-01-01')

        if df.empty:
            return render_template('index.html', error="Invalid Symbol or No Data Found")

        data = df[['Close']].values
        scaler = MinMaxScaler(feature_range=(0, 1))
        data_scaled = scaler.fit_transform(data)

        train_size = int(len(data_scaled) * 0.8)
        train_data = data_scaled[:train_size]

        model = create_model(train_data)

        last_60_days = data_scaled[-60:]
        input_data = last_60_days.reshape((1, 60, 1))
        pred_price = model.predict(input_data)[0][0]
        prediction = scaler.inverse_transform([[pred_price]])[0][0]

        df['Close'].plot(figsize=(10, 5))
        plt.title(f"{symbol} Stock Closing Prices")
        plt.xlabel("Date")
        plt.ylabel("Close Price")
        plt.tight_layout()
        plt.savefig("static/plot.png")
        plt.close()
        plot_url = "static/plot.png"

    return render_template('index.html', prediction=prediction, plot_url=plot_url)


if __name__ == '__main__':
    app.run(debug=True)
