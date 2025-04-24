# 주차 요금 계산기 만들기
# 사용자가 입력한 주차 시간을 기준으로 총 주차요금을 계산해 주는 프로그램
# 전제 조건
# 기본요금: 1시간 이내 5000원
# 1시간 초과시: 10분마다 500원 추가
# 24시간 이상 주차시: 하루 최대 30000원

# clock = int(input("주차 시간을 입력하세요(분 단위): "))
# fee = 0

# def calcul(n):
#     global fee
#     if n <= 60:
#         fee = 5000
#     elif n > 60:
#         fee = 5000 + ((n - 60) // 10) * 500
#     elif n >= 60 * 24:
#         fee = 30000
#     return fee

# last_fee = calcul(clock)
# print(f"> 주차 요금은 {last_fee}입니다.")

def calcul(n):
    if n >= 60 * 24:
        return 30000
    elif n > 60:
        return 5000 + ((n - 60) // 10) * 500
    else:
        return 5000

clock = int(input("주차 시간을 입력하세요(분 단위): "))
last_fee = calcul(clock)
print(f"> 주차 요금은 {last_fee}원입니다.")

# 24시간 이상 주차했을 때에 추가요금을 받는 소스 코드
# def calcul(n):
#     daily_fee = 30000

#     if n >= 60 * 24:
#         days = n // 1440
#         rest = n % 1440

#         # 나머지 시간 요금 계산
#         if rest <= 60:
#             extra = 5000
#         else:
#             extra = 5000 + ((rest - 60) // 10) * 500

#         return daily_fee * days + extra

#     elif n > 60:
#         return 5000 + ((n - 60) // 10) * 500
#     else:
#         return 5000