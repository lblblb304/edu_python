# 숫자 맞히기 게임
# 사용자가 숫자를 입력하면 컴퓨터가 "업", "다운", "정답"을 알려주는 게임
# 1~100사이의 정답 숫자 맞히기(일단 랜덤없이 고정값)

i = 1

while True:
    num = int(input("숫자를 입력해주세요: "))

    if num < 34:
        print("업!")
        i += 1
        continue
    elif num > 34:
        print("다운!")
        i += 1
        continue
    else:
        print("정답!")
        print(f"{i}번 만에 맞추셨습니다!")
        break