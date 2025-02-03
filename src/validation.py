from sklearn.metrics import mean_absolute_error

def validate_forecast(df, train_end_date):
    from prophet import Prophet
    import pandas as pd

    # Prepare data for Prophet
    df = df.rename(columns={"Ski Day": "ds", "valid_tickets": "y"})
    df["ds"] = pd.to_datetime(df["ds"])

    # Split the data
    train = df[df["ds"] <= train_end_date]
    test = df[df["ds"] > train_end_date]

    # Train the model
    model = Prophet(yearly_seasonality=True, daily_seasonality=False)
    model.fit(train)

    future = model.make_future_dataframe(periods=len(test))
    forecast = model.predict(future)

    # Calculate mse
    test_actual = test["y"].values
    test_predicted = forecast["yhat"][-len(test):].values
    mae = mean_absolute_error(test_actual, test_predicted)
    return mae, forecast
