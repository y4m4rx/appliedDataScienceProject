#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 15:36:31 2019

@author: Yasin
"""

### LSTM
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


dataset_train = pd.read_csv("df_train.csv")
training_set = dataset_train.iloc[:, -1:].values


#Feature Scaling
sc = MinMaxScaler(feature_range=(0,1))
training_set_scaled = sc.fit_transform(training_set)

# Creating a data structure with 30 timestamps and 1 output

X_train = []
y_train = []
useData = 60


for i in range(useData,len(training_set_scaled)):
    X_train.append(training_set_scaled[i-useData:i,0])
    y_train.append(training_set_scaled[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)

test_a = X_train
test_b = X_train.shape[0]
test_c = X_train.shape[1]

# Reshape for folfilling the Keras Layers --> 3 Dimensionen (all data, steps (useData),)
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1],1))


# Part 2 - Buling the RNN

# Importing the Keras libaries and packages
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

# Neuronce per layer --> we could expirement with that
first_layer = 50
second_layer = 50
third_layer = 50
fourth_layer = 50


# Initialisingt the RNN
regressor = Sequential()

# Adding the first LSTM Layer and some Droput regularisation
regressor.add(LSTM(units = first_layer, return_sequences = True, input_shape = (X_train.shape[1],1)))
regressor.add(Dropout(0.2))

# Adding the second LSTM Layer and some Droput regularisation
regressor.add(LSTM(units = second_layer, return_sequences = True))
regressor.add(Dropout(0.2))

# Adding the third LSTM Layer and some Droput regularisation
regressor.add(LSTM(units = third_layer, return_sequences = True))
regressor.add(Dropout(0.2))

# Adding the fourth LSTM Layer and some Droput regularisation
regressor.add(LSTM(units = fourth_layer))
regressor.add(Dropout(0.2))

# Adding outputlayer
regressor.add(Dense(units=1))

# Compiling the RNN
regressor.compile(optimizer = 'adam', loss = 'mean_squared_error') # check optimisers # what kind of 

# Fitting the RNN to the Training set
# epochs is how often it runs to reduce the loss
regressor.fit(X_train, y_train,epochs = 25, batch_size=32)


# Part 3 - Making the predictions and visualising the results
forcast = 30

# Getting prices for the set intervall (one_Day, one_week ..)
dataset_test = pd.read_csv("df_test.csv")
test_set = dataset_test.iloc[:, -1:].values


# Getting the predictet stockprice for intervall (one_Day, one_week ..)
dataset_total = pd.concat((dataset_train["Price"], dataset_test["Price"]), axis=0, ignore_index=True)
inputs = dataset_total[len(dataset_total)-len(dataset_test)-useData:].values
#inputs = dataset_total[len(dataset_total)-useData:].values
inputs = inputs.reshape(-1,1)
inputs = sc.transform(inputs)
X_test = []
for i in range(useData,useData+forcast):
    X_test.append(inputs[i-useData:i,0])
    #print(x)
X_test = np.array(X_test)
a = X_test.copy()
X_test = np.reshape(X_test, (X_test.shape[0],X_test.shape[1],1))
predicted_eth_price = regressor.predict(X_test)
predicted_eth_price = sc.inverse_transform(predicted_eth_price) # --> invers transform the Normalisation


# Ploting my results
pred= pd.DataFrame(predicted_eth_price,columns=["Price"])
pred

tmp = pd.concat((dataset_train["Price"], dataset_test["Price"], pred["Price"]), axis=0, ignore_index=True)

#plt.plot(tmp[:-test],color = "green", label = 'Training Data ETH Price')
#plt.plot(tmp[-test:],color = "red", label = "Test Data ETH Price")
#plt.plot(tmp[-len(predicted_eth_price):],color = "blue", label = "Predicted Data ETH Price")
plt.plot(test_set, color = 'red', label = 'Real ETH Price')
#plt.plot(training_set[:-one_month], color = "green", label = 'ETH Test')
plt.plot(predicted_eth_price, color = 'blue', label = 'Predictet ETH Price')
plt.title('ETH Price Prediction')
plt.xlabel('Time')
plt.ylabel('ETH Price')
plt.legend()
plt.show()

Margherita
Botanikus
Sucuk