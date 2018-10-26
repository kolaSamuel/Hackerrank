import urllib.request
from sklearn import linear_model
import numpy as np
from matplotlib.pyplot import *

url = "https://s3.amazonaws.com/hr-testcases/399/assets/trainingdata.txt"

with urllib.request.urlopen(url) as response:
    file = response
    train_data = np.array([line.decode('utf-8').strip().split(',') for line in file.readlines()], float)
    filtered_data = np.array([x for x in train_data if x[-1] < 8.00])

model = linear_model.LinearRegression()
model.fit(filtered_data[:, 0].reshape(-1, 1), filtered_data[:, -1])
print(model.coef_, model.intercept_)

# figure(1)
# scatter(train_data[:, 0], train_data[:, -1])
# scatter(filtered_data[:, 0], filtered_data[:, -1])
# show()
