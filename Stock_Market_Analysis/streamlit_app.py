import streamlit as st
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Load the dataset
def load_data():
    data_path = 'TataMotorsFinal.csv'  # Path to your dataset
    try:
        data = pd.read_csv(data_path, parse_dates=['Date'], index_col='Date')
        return data
    except FileNotFoundError:
        st.error("Dataset file not found. Ensure 'TataMotorsFinal.csv' is in the same directory.")
        return None

data = load_data()

if data is not None:
    # App Title
    st.title("Tata Motors Stock Price Prediction Using Prophet")

    # Sidebar for user input
    st.sidebar.header("Forecast Parameters")
    forecast_days = st.sidebar.number_input("Number of Days to Predict", min_value=1, max_value=365, value=30)

    # Display the dataset
    st.subheader("Dataset Overview")
    st.write(data.head())

    # Prepare data for Prophet
    df = data.reset_index()[['Date', 'Close']]
    df.rename(columns={'Date': 'ds', 'Close': 'y'}, inplace=True)

    # Plot historical data
    st.subheader("Historical Stock Prices")
    st.line_chart(data['Close'])

    # Forecasting using Prophet
    st.subheader("Prophet Model Predictions")
    if st.sidebar.button("Generate Forecast"):
        try:
            # Initialize and fit the Prophet model
            model = Prophet()
            model.fit(df)

            # Create a DataFrame for future dates
            future = model.make_future_dataframe(periods=forecast_days)
            forecast = model.predict(future)

            # Rename columns in the forecast DataFrame
            forecast_renamed = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].copy()
            forecast_renamed.columns = ['date', 'predicted_price', 'lower_price', 'higher_price']

            # Plot the forecast with custom colors and labels
            fig1 = model.plot(forecast)
            plt.title('Prophet Model Forecast')
            plt.xlabel('Date')
            plt.ylabel('Stock Price')

            # Customize the legend and colors
            plt.plot(forecast['ds'], forecast['yhat'], label='Predicted Price', color='blue', linewidth=2)
            plt.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='gray', alpha=0.3, label='Forecast Uncertainty')

            # Add a legend
            plt.legend()

            # Display the plot in the app
            st.pyplot(fig1)

            # Show forecasted values with the new column names
            st.subheader("Forecast Data")
            st.write(forecast_renamed.tail(forecast_days))

        except Exception as e:
            st.error(f"Error during forecasting: {e}")

if __name__ == "__main__":
    # Any initialization code or app launch logic goes here
    pass
