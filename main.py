import os
from src.data_handler import load_sql_file_to_dataframe
from src.forecasting import forecast_sales, save_forecast_to_csv
from src.validation import validate_forecast

# Define paths
# db_file_path = os.path.join("..", "data", "tickets.db") this did not work unforetunetly
db_file_path=db_file_path = r"C:\Users\miriyneg\pythonProject3\coding-challenge-data-science-public\data\tickets.db"

forecast_output_file = "forecast_results.csv"

if __name__ == "__main__":
    data = load_sql_file_to_dataframe(db_file_path)

    if data is not None:
        forecast = forecast_sales(data)

        # Save the forecast results
        save_forecast_to_csv(forecast, forecast_output_file)

        # Validate the model
        train_end_date = "2021-12-31"
        mae, _ = validate_forecast(data, train_end_date)
        print(f"Validation MAE: {mae}")
    else:
        print("Failed to load data. Exiting...")



