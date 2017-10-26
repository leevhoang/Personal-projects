# Lee Hoang
# 23 October 2017
# Machine Learning Project
#
# This file contains code for a simple linear regression model. It will predict the high score of gamers with certain years
# of gaming experience for a particular game.
#

# Import the libaries required for machine learning.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import the dataset containing the gamers' years of gameplay experience and their high scores.
dataset = pd.read_csv('GameplayData.csv')
X = dataset.iloc[:, :-1].values # Column containing the years of gameplay experience
y = dataset.iloc[:, 1].values # Column containing the player's high score.

# Split the dataset into the Training set and Test set.
# The best split ratio is 80:20: 80% of the data goes into the training set
# and 20% of the data goes into the test set.
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
# This will ensure that variables are scaled in the same way.
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)

# Fit SLR to the Training Set.
from sklearn.linear_model import LinearRegression
regressor = LinearRegression() # Create an object of the LR class.
regressor.fit(X_train, y_train) # Fit the regressor to the training set.

# Predicting the Test set results. Some will be overestimated and some will be underestimated.
y_pred = regressor.predict(X_test)

# Visualize the results of predicting the training set results.
plt.scatter(X_train, y_train, color = 'red') # Plot the observation points. They are in red.
plt.plot(X_train, regressor.predict(X_train), color = 'blue') # Plot the regression line. X = observations, y = predictions of the training test results.
plt.title('High Score vs Gameplay Time (Training Set)') # This is the title of the plot.
plt.xlabel('Gameplay Time (Years)') # Label for the X-axis of the plot.
plt.ylabel('High Score') # Label for the y-axis.
plt.show() # Show the plot after setting it up.