# appliedDataScienceProject


**Problem Statement**:
Predicting the Closing price of a stock is a commun field for ml. 
Predicting the Ethereum Price based on its network data is an interesting problem. 
For that we want to use different Forcasting Methods an want to evaluate them. Also we want to know which of the features are the most relevant ones. 

**Target Variable**: Ethereum Price

**Features**:
- Date(UTC)
-- Date of Record
- UnixTimeStamp
-- UnixTimeStamp of Record
- Supply
-- cummulatet amout of Ether
- MarketCap
-- Volume of all Ether in $ for the Record
- Price
-- Curren Price per Ether for the Record
- addressCount
-- Curren Addresses at time of Record
- txGrowth
-- How many new addresses were registered a the time of Record
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
**optional**:
- btcPrice
-- Bitcoin price for the record --> just out of curiosity
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
8. Prediction models
9. Evaluation
10. Documentation
-------------------------------------------------------------------

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
- https://hackernoon.com/wtf-is-the-blockchain-1da89ba19348
-------------------------------------------------------------------
