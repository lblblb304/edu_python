# 단어 길이 분석기
# 사용자가 입력한 문장에서 단어 별로 길이를 측정하고, 가장 긴 단어와 가장 짧은 단어를 출력하는 프로그램

# string = input("문장을 입력하세요: ")
# alp = string.split(" ")

# def analyzer(alp):
#     for i in range(alp):
#         length = len(alp[i])
#         print(f"{alp[i]} -> {length}글자")
#     print()

#     print(f"가장 긴 단어: {max.len(alp)} ({max.length}글자)")
#     print(f"가장 짧은 단어: {min.len(alp)} ({min.length}글자)")

# print(analyzer(alp))

# string = input("문장을 입력하세요: ")
# alp = string.split(" ")

# def analyzer(alp):
#     print("[단어 분석 결과]")
#     for word in alp:
#         print(f"{word} -> {len(word)}글자")

#     print()
#     print(f"가장 긴 단어: {max(alp, key=len)} ({len(max(alp, key=len))}글자)")
#     print(f"가장 짧은 단어: {min(alp, key=len)} ({len(min(alp, key=len))}글자)")
#     return alp

# print(analyzer(alp))

string = input("문장을 입력하세요: ").strip() # 입력 값 양쪽 공백 제거
alp = string.split(" ")

def analyzer(alp):
    print("[단어 분석 결과]")
    for word in alp:
        print(f"{word} -> {len(word)}글자")

    print()
    print(f"가장 긴 단어: {max(alp, key=len)} ({len(max(alp, key=len))}글자)")
    print(f"가장 짧은 단어: {min(alp, key=len)} ({len(min(alp, key=len))}글자)")

analyzer(alp)