# 숫자 나누기 계산기(예외 처리 포함)
# 사용자에게 숫자 2개를 입력받고 나눗셈 결과를 출력하는데, 0으로 나누는 경우 에러 메시지를 출력하고 다시 입력받는 프로그램

while True:
    try:
        num1 = int(input("첫 번째 숫자를 입력하세요: "))
        num2 = int(input("두 번째 숫자를 입력하세요: "))
        print(f"결과: {num1} / {num2} = {num1 / num2}")
        break
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다!")
    except ValueError:
        print("숫자만 입력해 주세요.")
    except Exception as exception:
        print("미리 파악하지 못한 예외가 발생하였습니다.")
        print(type(exception), exception)

# 첫 숫자가 올바르게 들어 왔을 때, 두 번째 숫자만 반복해서 다시 받는 코드
# while True:
#     try:
#         if 'num1' not in locals():
#             num1 = int(input("첫 번째 숫자를 입력하세요: "))  # ← 여기서 잘못 입력하면 except로 감
#
#         num2 = int(input("두 번째 숫자를 입력하세요: "))
#         result = num1 / num2
#         break
#
#     except ZeroDivisionError:
#         print("0으로 나눌 수 없습니다! 다시 입력해 주세요.")
#     except ValueError:
#         print("숫자만 입력해 주세요.")