import numpy as np
import matplotlib.pyplot as plt

# 랜덤 시드 설정 (재현 가능성)
np.random.seed(42)

# 데이터 생성
x = np.linspace(0, 1, 100)  # 0에서 1 사이의 100개 점
y_true = np.sin(2 * np.pi * x)  # sin(2πx) 함수 값
noise = np.random.normal(0, 0.1, size=x.shape)  # 평균 0, 표준편차 0.1인 가우시안 노이즈
y_noisy = y_true + noise  # 노이즈가 추가된 데이터

# 데이터 시각화
plt.figure(figsize=(10, 5))
plt.plot(x, y_true, label="True function (sin(2πx))", color="blue")
plt.scatter(x, y_noisy, label="Noisy data", color="red", alpha=0.6)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Artificial Data with Noise using sin(2πx)")
plt.legend()
plt.grid()
plt.show()
