# 김밥천국 주문 계산기
# 전제조건 
# 김밥 : 2500원
# 라면 : 3500원
# 떡볶이 : 4000원

kimbab = int(input("김밥을 몇 개 주문하시겠습니까?> ")) * 2500
rameon = int(input("라면을 몇 개 주문하시겠습니까?> ")) * 3500
tteok = int(input("떡볶이를 몇 개 주문하시겠습니까?> ")) * 4000

price = kimbab + rameon + tteok

print("총 가격은", price, "원 입니다.")