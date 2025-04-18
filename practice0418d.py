# 이름 반복 출력기
# 이름과 반복 횟수를 입력 받고, 이름을 그 횟수만큼 한 줄에 출력하세요.

name = input("이름을 입력하세요: ")
repeat = int(input("몇 번 반복할까요?: "))

print("출력: {}".format(name * repeat))