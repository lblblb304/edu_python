# 심플 점수 등급 평가기
# 점수를 입력 받고, 기준에 따라 등급을 출력

score = int(input("점수를 입력해 주세요: "))

if score >= 90:
    print("A등급입니다.")
elif score >= 80:
    print("B등급입니다.")
elif score >= 70:
    print("C등급입니다.")
elif score >= 60:
    print("D등급입니다.")
else:
    print("F등급입니다.")