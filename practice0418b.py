# 초간단 BMI 계산기
# BMI 지수를 계산하고 출력하는 프로그램

height = float(input("키를 입력해 주세요 (cm단위): ")) / 100
weight = int(input("몸무게를 입력해 주세요 (kg단위): "))

BMI = weight / (height ** 2)

print(f"당신의 BMI지수는 {BMI:.2f} 입니다.")