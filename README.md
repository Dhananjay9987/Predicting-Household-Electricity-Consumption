# Predicting-Household-Electricity-Consumption

This project demonstrates how to predict hourly electricity consumption using Linear Regression with historical consumption data.
The dataset contains synthetic electricity consumption values across different hours of the day.

# Project Structure

├── electricity_data.csv   
├── main.py                
└── README.md      

# Steps in the Code

1. Import Libraries & Load Dataset
   a. Uses pandas, matplotlib, and scikit-learn for data analysis, visualization, and modeling.
   b. Loads the dataset electricity_data.csv.

2. Feature Engineering
   o Creates a new column prev_hour (consumption of the previous hour).
   o Uses hour and prev_hour as features.
   o Drops missing values after shifting.

3. Train-Test Split
   o Splits the dataset into training (80%) and testing (20%) sets.
   o No shuffling to maintain time-series order.

4. Train Model
   o Trains a Linear Regression model on training data.
   o Predicts electricity consumption on test data.

5. Evaluate Model
   o Metrics used: Mean Absolute Error (MAE), R² Score
   o Prints performance results.

6. Visualization
   o Plots Actual vs Predicted electricity consumption values for test data.

# Output

1. Metrics:
   o Mean Absolute Error: ~4.5
   o R² Score: ~0.80

2. Visualization:
   o A line chart showing actual consumption vs predicted consumption.

# Requirements

  o Install dependencies before running: pip install pandas matplotlib scikit-learn

# How to Run

1. Run the script:
   o python main.py
   o View the prediction results and chart.

# Future Improvements
  o Add seasonal/weekly variations in dataset.
  o Try advanced models (Random Forest, LSTM).
  o Deploy model as a web app for real-time prediction.




