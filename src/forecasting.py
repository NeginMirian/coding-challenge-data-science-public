from prophet import Prophet
import pandas as pd

def forecast_sales(df):

    # Data prepation
    df = df.rename(columns={"Ski Day": "ds", "valid_tickets": "y"})
    df["ds"] = pd.to_datetime(df["ds"])

    # Initialize and fit the Prophet model
    model = Prophet(yearly_seasonality=True, daily_seasonality=False)
    model.fit(df)

    # Define the forecast period (2022-12-10 to 2023-04-15)
    future = pd.date_range(start="2022-12-10", end="2023-04-15", freq="D")
    future_df = pd.DataFrame(future, columns=["ds"])

    # Generate predictions
    forecast = model.predict(future_df)
    return forecast

    # Create a future dataframe for the forecast period
    future = model.make_future_dataframe(periods=forecast_periods)
    forecast = model.predict(future)
    return forecast

def save_forecast_to_csv(forecast, output_file):
    forecast_filtered = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]
    forecast_filtered.to_csv(output_file, index=False)
    print(f"Forecast results saved to {output_file}")


