# 2차원 리스트 평탄화
# 리스트가 중첩되어 있을 때 중첩을 제거하는 처리를 리스트 평탄화(list flatten)라고 한다
# ex) [1, 2, [3, 4], 5, [6, 7], [8, 9]] -> [1, 2, 3, 4, 5, 6, 7, 8, 9]

#list_a = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
#
#for i in range(0, len(list_a)):
#   if type(list_a[i]) == list:
#       for j in range(0, len(list_a[i])):
#           list_a.insert(int(list_a[i]), list_a[i][j])
#       del list_a[i]
#
#print(f"[1, 2, [3, 4], 5, [6, 7], [8, 9]]를 평탄화 하면\n{list_a}입니다")

a = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
output = []

for i in a:
    if type(i) == list:
        # 요소가 리스트라면: 또 반복해서 요소를 추가합니다.
        for j in i:
            output.append(j)
    else:
        # 요소가 숫자라면: 그냥 추가합니다.
        output.append(i)

print(f"{a}를 평탄화 하면")
print(f"{output}입니다")