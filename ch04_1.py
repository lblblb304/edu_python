# 리스트에서 몇가지 종류 숫자가 사용되었는지 구하는 프로그램
# 딕셔너리를 활용
list_a = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
dictionary = {}

for i in list_a:
    if i not in dictionary:
        dictionary[i] = 0
    dictionary[i] += 1

print(f"{list_a}에서\n사용된 숫자의 종류는 {len(dictionary)}개입니다.")
print(f"참고: {dictionary}")