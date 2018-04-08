from sklearn import linear_model as lm
from numpy import array
physics_history = array([input().split()[2:] for _ in range(2)], int)

model = lm.LinearRegression()
model.fit([[x] for x in physics_history[0]], physics_history[1])
print(model.coef_)
print(model.intercept_)
