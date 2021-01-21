from sklearn import datasets
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_absolute_error


loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_y = loaded_data.target


model = LinearRegression()

model.fit(data_X, data_y)


predict = model.predict(data_X)

accuracy = mean_absolute_error(data_y,predict)

print(accuracy)