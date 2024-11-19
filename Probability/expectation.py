import numpy as np

# 데이터 샘플
data = [1, 2, 3, 4, 5]

# 기댓값 계산
expected_value = np.mean(data)
print(f"기댓값: {expected_value}")

# 두 변수 데이터
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 공분산 계산
covariance = np.cov(x, y, bias=True)[0, 1]
print(f"공분산: {covariance}")
