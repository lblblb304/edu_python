# 문자열 내 단어 수 세기
# 문장속의 특정 글자가 몇 번 나오는지 세보는 프로그램

sen = input("문장을 입력하세요: ")
alp = input("세어볼 글자를 입력하세요: ")

value = int(sen.count(alp))

print(f"출력: '{alp}'는/은 {value}번 등장합니다.")