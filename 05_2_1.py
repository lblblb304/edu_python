minimum = 2
maximum = 10
humans = 100
memo = {}

def tsplit(rest, sit):
    key = str([rest, sit])
    # 종료 조건
    if key in memo:
        return memo[key]
    if rest < 0:
        return 0
    if rest == 0:
        return 1
    # 재귀 처리
    count = 0
    for i in range(sit, maximum + 1):
        count += tsplit(rest - i, i)
    # 메모화 처리
    memo[key] = count
    # 종료
    return count

print(tsplit(humans, minimum))