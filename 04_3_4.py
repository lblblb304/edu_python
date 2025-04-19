max_value = 0
a = 0
b = 0

for i in range(1, 99 +1):
    j = 100 - i

    # 최댓값 구하기
    k = i * j
    if max_value <= k:
        max_value = k
        a = i
        b = j

print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))

for i in range(1, 100 // 2 + 1):
    j = 100 - i

    # 최댓값 구하기
    current = i + j
    if max_value < current:
        a = i
        b = j
        max_value = current

print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))