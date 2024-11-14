import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 인공 데이터 생성
np.random.seed(42)
x_train = np.random.rand(20, 1)  # 0에서 1 사이의 20개 훈련 데이터
y_train = np.sin(2 * np.pi * x_train) + np.random.normal(0, 0.1, size=x_train.shape)

x_test = np.linspace(0, 1, 100).reshape(-1, 1)  # 0에서 1 사이의 100개 테스트 데이터
y_test = np.sin(2 * np.pi * x_test)

# 다항 회귀 모델 학습 및 평가
degrees = [0, 1, 3, 6, 9]  # 차수 M
train_errors = []
test_errors = []

plt.figure(figsize=(15, 10))

for i, degree in enumerate(degrees):
    # 다항 특징 생성
    poly = PolynomialFeatures(degree)
    x_poly_train = poly.fit_transform(x_train)
    x_poly_test = poly.transform(x_test)

    # 선형 회귀 모델 학습
    model = LinearRegression()
    model.fit(x_poly_train, y_train)

    # 예측값 계산
    y_train_pred = model.predict(x_poly_train)
    y_test_pred = model.predict(x_poly_test)

    # 오차 계산 (MSE)
    train_mse = mean_squared_error(y_train, y_train_pred)
    test_mse = mean_squared_error(y_test, y_test_pred)
    train_errors.append(train_mse)
    test_errors.append(test_mse)

    # 시각화
    plt.subplot(2, 3, i + 1)
    plt.scatter(x_train, y_train, color='red', label='Train Data')
    plt.plot(x_test, y_test, color='green', label='True Function')
    plt.plot(x_test, y_test_pred, color='blue', label=f'Predicted (M={degree})')
    plt.title(f'Degree {degree}\nTrain MSE: {train_mse:.4f}, Test MSE: {test_mse:.4f}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()

# 학습 오차와 테스트 오차 비교
plt.subplot(2, 3, 6)
plt.plot(degrees, train_errors, label='Train MSE', marker='o')
plt.plot(degrees, test_errors, label='Test MSE', marker='o')
plt.xlabel('Polynomial Degree (M)')
plt.ylabel('Mean Squared Error (MSE)')
plt.title('Train vs Test MSE')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
