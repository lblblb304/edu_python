# 구의 부피와 겉넓이를 구하는 프로그램 만들기
pi = 3.141592
r = float(input("구의 반지름을 입력해주세요: "))
volume = 4 / 3 * pi * (r ** 3)
area = 4 * pi * (r ** 2)

print("= 구의 부피는", volume, "입니다.")
print("= 구의 겉넓이는", area, "입니다.")