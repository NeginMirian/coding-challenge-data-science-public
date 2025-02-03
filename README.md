# Data Science Coding Challenge
Project Structure
The project is organized into the following key components:

data/: Contains the SQLite database (tickets.db) with historical ticket sales data.

src/: Contains the core Python scripts for data handling, forecasting, and validation:

data_handler.py: Handles loading data from the SQLite database.

forecasting.py: Implements the forecasting logic using Prophet.

validation.py: Validates the model by splitting data into training and testing sets.

main.py: The main script that orchestrates the workflow.

forecast_results_2022_2023.csv: The output file containing the forecasted ticket sales.

The forecast results include:
Date (ds): The forecasted date.

Predicted Sales (yhat): The predicted daily ticket sales.

Lower Bound (yhat_lower): The lower confidence interval for the prediction.

Upper Bound (yhat_upper): The upper confidence interval for the prediction.

Model Choice:
Prophet was chosen because it handles seasonality and trends well, which are important for ski ticket sales.
Validation:
The model was validated by splitting data into training (2016–2021) and testing (2022), and the accuracy was measured using the Mean Absolute Error (MAE).

Next Steps
If given more time, we could improve the project by:

Incorporating external factors like weather data or holidays.

Tuning the model hyperparameters for improved accuracy.

Automating the validation process to refine the model further.