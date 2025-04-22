# 구구단 출력기
# 사용자가 숫자를 입력하면, 그 숫자의 구구단을 출력하는 프로그램

while True:
    num = int(input("1~9까지 숫자중에 하나를 입력하세요: "))

    if 1 <= num <= 9:
        for i in range(1, 10):
            print(f"{num} * {i} = {num * (i)}")
        break
    else:
        print("입력한 숫자가 1~9안에 숫자가 아닙니다.")
        continue