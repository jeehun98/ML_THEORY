import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error

# 인공 데이터 생성
np.random.seed(42)
x_train = np.random.rand(20, 1)  # 0에서 1 사이의 20개 훈련 데이터
y_train = np.sin(2 * np.pi * x_train) + np.random.normal(0, 0.1, size=x_train.shape)

x_test = np.linspace(0, 1, 100).reshape(-1, 1)  # 0에서 1 사이의 100개 테스트 데이터
y_test = np.sin(2 * np.pi * x_test)

# 다항 차수 설정
degree = 9
poly = PolynomialFeatures(degree)
x_poly_train = poly.fit_transform(x_train)
x_poly_test = poly.transform(x_test)

# 모델 정의
models = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression (L2)": Ridge(alpha=1.0),  # L2 정규화 (alpha는 λ 값)
    "Lasso Regression (L1)": Lasso(alpha=0.01)  # L1 정규화 (alpha는 λ 값)
}

# 시각화 설정
plt.figure(figsize=(18, 5))

# 각 모델에 대해 학습 및 평가
for i, (name, model) in enumerate(models.items()):
    # 모델 학습
    model.fit(x_poly_train, y_train)

    # 예측값 계산
    y_train_pred = model.predict(x_poly_train)
    y_test_pred = model.predict(x_poly_test)

    # MSE 계산
    train_mse = mean_squared_error(y_train, y_train_pred)
    test_mse = mean_squared_error(y_test, y_test_pred)

    # 시각화
    plt.subplot(1, 3, i + 1)
    plt.scatter(x_train, y_train, color='red', label='Train Data')
    plt.plot(x_test, y_test, color='green', label='True Function')
    plt.plot(x_test, y_test_pred, color='blue', label=f'Predicted ({name})')
    plt.title(f"{name}\nTrain MSE: {train_mse:.4f}, Test MSE: {test_mse:.4f}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()

plt.tight_layout()
plt.show()
