# Electricity Consumption Prediction using Linear Regression

This project demonstrates how to predict hourly electricity consumption using Linear Regression with historical consumption data.
The dataset contains synthetic electricity consumption values across different hours of the day.

# Project Structure

├── electricity_data.csv  
├── main.py                
└── README.md             

# Steps in the Code
1. Import Libraries & Load Dataset

   * ses pandas, matplotlib, and scikit-learn for data analysis, visualization, and modeling.

   * Loads the dataset electricity_data.csv.

2. Feature Engineering

   * Creates a new column prev_hour (consumption of the previous hour).

   * Uses hour and prev_hour as features.

   * Drops missing values after shifting.

3. Train-Test Split

   * Splits the dataset into training (80%) and testing (20%) sets.

   * No shuffling to maintain time-series order.

4. Train Model

   * Trains a Linear Regression model on training data.

   * Predicts electricity consumption on test data.

5. Evaluate Model

   1. Metrics used:

     * Mean Absolute Error (MAE)

     * R² Score

   2. Prints performance results.

6. Visualization

   * Plots Actual vs Predicted electricity consumption values for test data.

# Output

   1. Metrics:

       * Mean Absolute Error: ~4.5
       * R² Score: ~0.80


   2. Visualization:
       *A line chart showing actual consumption vs predicted consumption.

# Requirements

   1. Install dependencies before running:
        pip install pandas matplotlib scikit-learn

# How to Run

   1. Run the script:
 
      python main.py


   2. View the prediction results and chart.

# Future Improvements

   1. Add seasonal/weekly variations in dataset.

   2. Try advanced models (Random Forest, LSTM).

   3. Deploy model as a web app for real-time prediction.

# Author

 Dhananjay Gupta
