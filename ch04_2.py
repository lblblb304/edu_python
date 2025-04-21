# 염기의 개수
# DNA는 A, T, G, C라는 4가지 요소로 구성되어있다. 각 염기의 개수를 세어보자.
# ex) ctacaatgtcagtacccattgcattagccgg
dna = input("염기 서열을 입력해주세요: ")
list_dna = {
    "a": 0,
    "t": 0,
    "g": 0,
    "c": 0
}

for i in dna:
    list_dna[i] += 1

for key in list_dna:
    print(f"{key}의 개수: {list_dna[key]}")