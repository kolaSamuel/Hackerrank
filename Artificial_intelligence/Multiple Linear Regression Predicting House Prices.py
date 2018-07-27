import numpy as np
from sklearn import linear_model as lm

F, N = list(map(int, input().split()))
train_data = np.array([input().split() for _ in range(N)], float)
T = int(input())
test_data = np.array([input().split() for _ in range(T)], float)

model = lm.LinearRegression()

model.fit(train_data[:, :-1], train_data[:, -1])
result = model.predict(test_data)
print(*result, sep='\n')
