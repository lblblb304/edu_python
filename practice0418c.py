# 비밀번호 마스킹 프로그램
# 사용자가 입력한 비밀번호를 마스킹(*)처리해서 출력하기

pwd = input("비밀번호를 입력하세요: ")

len = len(pwd)
masking = "*" * int(len)

print(f"당신의 비밀번호는 {masking} ({len}자리)입니다.")