import numpy as np
import matplotlib.pyplot as plt

# 원래의 PDF (표준 정규분포)
def original_pdf(x):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

# 변환된 PDF (y = 2x)
def transformed_pdf(y):
    # x = y / 2, 야코비안 = 1/2
    x = y / 2
    jacobian = 1 / 2
    return original_pdf(x) * jacobian

# x와 y 범위
x = np.linspace(-4, 4, 1000)
y = np.linspace(-8, 8, 1000)

# PDF 계산
original_values = original_pdf(x)
transformed_values = transformed_pdf(y)

# 그래프 그리기
plt.figure(figsize=(10, 6))

# 원래의 PDF
plt.plot(x, original_values, label="Original PDF (x ~ N(0,1))", linewidth=2)

# 변환된 PDF
plt.plot(y, transformed_values, label="Transformed PDF (y = 2x)", linewidth=2, linestyle="--")

# 그래프 꾸미기
plt.title("Effect of Variable Transformation on PDF", fontsize=16)
plt.xlabel("Variable", fontsize=14)
plt.ylabel("Probability Density", fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)
plt.show()
