import numpy as np
from sklearn import linear_model as lm
from sklearn import preprocessing as pp

F, N = list(map(int,input().split()))
train_data = np.array([input().split() for _ in range(N)], float)
T = int(input())
test_data = np.array([input().split() for _ in range(T)], float)

to_poly = pp.PolynomialFeatures(3, include_bias=False)
model = lm.LinearRegression()

model.fit(to_poly.fit_transform(train_data[:, :-1]), train_data[:, -1])
result = model.predict(to_poly.fit_transform(test_data))
print(*result)
