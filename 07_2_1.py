# 소수를 구하는 모듈을 설치후에 실행해보는 문제
from sympy import primerange

print(f"100부터 1000사이의 소수의 개수는 {len(list(primerange(100, 1000)))}개 입니다.")
print()
print(len(list(primerange(100, 1000))))