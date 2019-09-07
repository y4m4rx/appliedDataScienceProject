# appliedDataScienceProject


**Raw data source**: https://etherscan.io/charts & https://www.investing.com/crypto/bitcoin/historical-data

**Helpful Links**: :grin:
- https://towardsdatascience.com/machine-learning-general-process-8f1b510bd8af
- https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end=20190612
- https://www.kaggle.com/arsenalist/bitcoin-prices-prediction
- https://www.kaggle.com/myonin/bitcoin-price-prediction-by-arima
- https://www.kaggle.com/someadityamandal/bitcoin-time-series-forecasting
- https://www.youtube.com/watch?v=KvZ2KSxlWBY&t=752s
- https://machinelearningmastery.com/time-series-forecasting/
- https://www.analyticsvidhya.com/blog/2018/02/time-series-forecasting-methods/
 
-------------------------------------------------------------------
**STEPS**:
1. Download raw data from https://etherscan.io/charts
2. Merge data (code uploaded)
3. Data Cleaning (Missing Values)
4. Explore & Handling the Data
  - Visualizations
  - Correlations
  - Handling outliers
  - Normilization
5. One-hot encoding for categorical data
6. Feature Selection
7. Grid search to determine the model hyper-parameters
8. Prediction models
9. Evaluation
10. Documentation
-------------------------------------------------------------------
*Yasin's input*:

Problem Statement:
Predicting the Closing price of a stock is a commun field for ml. 
Predicting the Ethereum Price based on its network data is an interesting problem. 
For that we want to use different Forcasting Methods an want to evaluate them. Also we want to know which of the features are the most relevant ones. 

Target Variable:
- Ethereum Price

Features:
- Ethereum Price
- Date
- Transaction count (per Day)
- Address count (per Day)
- Transaction Fee
- Gase Used (Gas is kind of transaction Fee)
- Name Registration

Other Possible Features:
- Bitcoin Price
- Lite Coin Price

Project Planning:

Maybe build a smal grafic to explain the project plan in a big picture
- Define Problem
- Collect Data
- Chosose Measure of Success
- Setting Evaluation Protocol
- Preparing the Data
- Developing Benchmark model
- Developing Better Model & Tunning its Hyperparameters (I think this is optional)
- Conclusion
-------------------------------------------------------------------
