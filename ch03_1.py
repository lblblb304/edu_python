# 간단한 대화 프로그램
msg = input("입력: ")

# 시간 기능 가져오기
import datetime

now = datetime.datetime.now()

if "안녕" in msg:
    print("> 안녕하세요.")
elif "몇 시" in msg:
    print(f"지금은 {now.hour}시입니다.")
else:
    print(msg)