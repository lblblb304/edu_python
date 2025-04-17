# 사용자가 입력한 "초"를 분과 초로 변환해주는 프로그램을 만들어보자.

print("초를 분과 초로 변환해줍니다")

sec = int(input("초를 입력해주세요> "))

min = str(sec // 60)
remainder = str(sec % 60)

print(min + "분" + remainder + "초 입니다.")