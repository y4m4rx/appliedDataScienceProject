# Applied Data Science Project


**Problem Statement**:
Predicting the price of a stock is a commun field for ml. 
Our problem setting is to predict the Ethereum Price for the next day, week and month based on its network data is an interesting problem. 
For that we want to use different Forcasting Methods an want to evaluate them. Also we want to know which of the features are the most relevant ones. 

**Target Variable**: Ethereum Price

**Models**:
- Autoregressive Integrated Moving Average (ARIMA)
- LSTM
- Holt Winter’s Exponential Smoothing (HWES) 
- FB Prophet

**Features**:
- Date (UTC)
-- Date of Record
- Supply
-- cummulatet amout of Ether
- addressCount
-- Current Addresses at time of Record
- txGrowth
-- How many new addresses were registered a the time of Record
- Difficulty
-- ?
- networkHash
-- ?
- networkUtilization
-- ?
- transactionFee
-- How much Transaction fee in average was on that Record
- avgGasPrice
-- Average Gas Price per Transaction
- blockCountReward
-- average block Reward for time of Record
- blockSize
-- averege block time for Record
- blockTime
-- Average block Time for the record (how long dose it take to "mine" one block)
- ethersupply
-- ?
- gasLimit
-- Average gas Limit for time of Recrod
- gasUsed
-- How much Gas was actually used
- uncles
-- How many uncles had the block (Uncles are blocks that are mined in parallel)
- btcPrice
-- ?
- Price
-- Curren Price per Ether for the Record
-------------------------------------------------------------------

**STEPS**:
1. Download raw data
2. Merge data
3. Data Cleaning (Missing Values)
4. Explore & Handling the Data
  - Visualizations
  - Correlations
  - Handling outliers
  - Normilization
5. One-hot encoding for categorical data
6. Feature Selection
7. Grid search to determine the model hyper-parameters
8. Stationarity of data
9. Prediction models
10. Evaluation
-------------------------------------------------------------------

**Raw data source**: https://etherscan.io/charts & https://www.investing.com/crypto/bitcoin/historical-data

**Helpful Links**: :grin:
- https://otexts.com/fpp2/
- https://www.youtube.com/watch?v=JntA9XaTebs
- https://www.youtube.com/playlist?list=PL8eNk_zTBST-dRBPxVlqsQjFVYB_IPaAR
- https://towardsdatascience.com/machine-learning-general-process-8f1b510bd8af
- https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end=20190612
- https://www.kaggle.com/arsenalist/bitcoin-prices-prediction
- https://www.kaggle.com/myonin/bitcoin-price-prediction-by-arima
- https://www.kaggle.com/someadityamandal/bitcoin-time-series-forecasting
- https://www.youtube.com/watch?v=KvZ2KSxlWBY&t=752s
- https://machinelearningmastery.com/time-series-forecasting/
- https://www.analyticsvidhya.com/blog/2018/02/time-series-forecasting-methods/
- https://hackernoon.com/wtf-is-the-blockchain-1da89ba19348

**libraries**:
- https://github.com/facebook/prophet/issues/892
- https://github.com/keras-team/keras/issues/4889
- https://github.com/tensorflow/tensorflow/issues/27935
-------------------------------------------------------------------

