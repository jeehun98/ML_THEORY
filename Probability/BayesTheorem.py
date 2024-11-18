import matplotlib.pyplot as plt
import numpy as np

# 확률 값 설정
P_A = 0.02
P_B_given_A = 0.9
P_B_given_not_A = 0.05

# 사건 B의 전체 확률 계산
P_not_A = 1 - P_A
P_B = P_B_given_A * P_A + P_B_given_not_A * P_not_A

# 다양한 P(A) 값에 대한 P(A|B) 계산
P_A_values = np.linspace(0, 0.1, 100)
P_A_given_B_values = (P_B_given_A * P_A_values) / (P_B_given_A * P_A_values + P_B_given_not_A * (1 - P_A_values))

# 그래프 그리기
plt.plot(P_A_values, P_A_given_B_values, label='P(A|B)')
plt.axvline(x=P_A, color='r', linestyle='--', label='P(A) = 0.02')
plt.title("P(A|B) vs. P(A)")
plt.xlabel("P(A)")
plt.ylabel("P(A|B)")
plt.legend()
plt.grid()
plt.show()
