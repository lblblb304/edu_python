# 하노이 탑
# <<혼자 공부하는 파이썬>> 354p

# 하노이 탑에서 필요한 요소를 모두 매개변수로 받습니다.
# 하노이탑(원판, "시작기둥"에서 "대상기둥"으로 "보조기둥"을 활용해서):
#     if 원판이 1개:
#         이동 from 시작기둥 to 대상기둥
#
#     if 원판이 2개이상:
#         # 아래의 원판을 제외하고, 시작 기둥에서 보조 기둥으로 이동합니다.
#         하노이탑(원판 - 1, "시작기둥"에서 "보조기둥"으로 "대상기둥"을 활용해서)
#         이동 from 시작 기둥 to 대상 기둥
#         # 아래의 원판을 제외하고, 보조 기둥에서 대상 기둥으로 이동합니다.
#         하노이탑(덩어리 - 1, "보조기둥"에서 "대상기둥"으로 "시작기둥"을 활용해서)

def hanoi(o, a, b, c):
    if o == 1:
        print(f"{a}탑 -> {b}탑")
    else:
        hanoi(o - 1, a, c, b)
        print(f"{a}탑 -> {b}탑")
        hanoi(o - 1, c, b, a)

obj = int(input("원판의 개수를 입력하세요: "))
hanoi(obj, "A", "B", "C")

# count = 0  # 이동 횟수 저장용

# def hanoi(o, a, b, c):
#     global count
#     if o == 1:
#         print(f"{a}탑 -> {b}탑")
#         count += 1
#     else:
#         hanoi(o - 1, a, c, b)
#         print(f"{a}탑 -> {b}탑")
#         count += 1
#         hanoi(o - 1, c, b, a)

# obj = int(input("원판의 개수를 입력하세요: "))
# hanoi(obj, "A", "B", "C")
# print(f"\n총 이동 횟수: {count}회")