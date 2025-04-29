# main.py
import my_calculator as mc

num_a = int(input("첫 번째 숫자를 입력하세요: "))
num_b = int(input("두 번째 숫자를 입력하세요: "))

print(f"더하기 결과: {mc.add(num_a, num_b)}")
print(f"빼기 결과: {mc.subtract(num_a, num_b)}")
print(f"곱하기 결과: {mc.multiply(num_a, num_b)}")
print(f"나누기 결과: {mc.divide(num_a, num_b)}")