# 현금 인출기 시뮬레이터
# 사용자가 인출할 금액을 입력하면 만 원, 오천 원, 천 원 단위로 지폐를 어떻게 나눠줄지 계산하는 프로그램

dict_won = {
    10000 : 0,
    5000 : 0,
    1000 : 0
}
sum_won = 0

while True:
    won = int(input("금액을 투입해주세요> "))

    if won >= 10000:
        tenthou = won // 10000
        dict_won[10000] = tenthou
        won %= 10000
    if won >= 5000:
        fivethou = won // 5000
        dict_won[5000] = fivethou
        won %= 5000
    if won >= 1000:
        thou = won // 1000
        dict_won[1000] = thou
        for i in dict_won:
            print(f"{i}원 : {dict_won[i]}장")
            sum_won += i * int(dict_won[i])
        print(f"총 지급금액은 {sum_won}입니다")
        break
    else:
        print("1000원 미만이면 인출할 수 없습니다")