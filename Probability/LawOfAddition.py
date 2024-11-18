# 상호 배타적인 경우
P_A = 0.3  # 사건 A의 확률
P_B = 0.4  # 사건 B의 확률

# 합의 법칙 (상호 배타적인 경우)
P_A_or_B = P_A + P_B
print(f"상호 배타적인 경우 P(A ∪ B) = {P_A_or_B:.2f}")

# 상호 배타적이지 않은 경우
P_A_and_B = 0.1  # 사건 A와 B가 동시에 발생할 확률

# 합의 법칙 (상호 배타적이지 않은 경우)
P_A_or_B_non_exclusive = P_A + P_B - P_A_and_B
print(f"상호 배타적이지 않은 경우 P(A ∪ B) = {P_A_or_B_non_exclusive:.2f}")
