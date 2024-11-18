# 사건 A와 B의 확률
P_A_and_B = 0.12  # 사건 A와 B가 동시에 발생할 확률
P_B = 0.3  # 사건 B의 확률

# 조건부 확률 계산
P_A_given_B = P_A_and_B / P_B

print(f"조건부 확률 P(A|B) = {P_A_given_B:.4f}")
