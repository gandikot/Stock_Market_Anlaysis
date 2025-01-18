# Stock_Market_Anlaysis

## Overview
This project explores and analyzes stock market data to uncover trends, visualize patterns, and build predictive models. The analysis includes comprehensive exploratory data analysis (EDA), time series forecasting, and machine learning techniques to predict stock prices.

## Features
- **Exploratory Data Analysis (EDA):** Visualizations to understand stock trends, correlations, and seasonality.
- **Feature Engineering:** Handling missing data, scaling, and creating new features.
- **Machine Learning Models:** Implementation of regression models, Random Forest, and Support Vector Machines (SVM).
- **Time Series Forecasting:** Using ARIMA, SARIMA, and Facebook Prophet for stock price prediction.

## Dataset
The dataset contains stock market data with the following columns:
- **Date:** The date of the stock prices.
- **Open, High, Low, Close:** Prices at different times of the day.
- **Volume:** The number of shares traded.

The project works with a CSV dataset located in the `data/` folder. A sample file is provided (`sample_data.csv`).

## Prerequisites
Install Python and the required dependencies listed in `requirements.txt`.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Stock_Market_Analysis.git
   cd Stock_Market_Analysis
   ```
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook:
   ```bash
   jupyter notebook Stock_Market_Analysis.ipynb
   ```

## Project Workflow
1. **Data Loading:** Import the historical stock market data.
2. **EDA:** Analyze trends with visualizations like line plots, heatmaps, and boxplots.
3. **Feature Engineering:** Handle missing values, scaling, and create new features for better modeling.
4. **Time Series Modeling:** 
   - ARIMA and SARIMA for autoregressive forecasting.
   - Facebook Prophet for seasonality and trend decomposition.
5. **Machine Learning Models:**
   - Random Forest for regression tasks.
   - Support Vector Machines for classification and regression.
6. **Evaluation:** Evaluate models with metrics like Mean Squared Error (MSE) and accuracy.

## Results
- Detailed insights into stock trends, correlations, and seasonality.
- Effective predictive models for stock price forecasting with high accuracy.


## Dependencies
The project uses the following libraries:
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `plotly`
- `scikit-learn`
- `statsmodels`
- `pmdarima`
- `prophet`
- `joblib`

Install these libraries with:
```bash
pip install -r requirements.txt
