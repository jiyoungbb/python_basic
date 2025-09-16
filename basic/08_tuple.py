food = ("피자", "햄버거", "치킨")
print(type(food))

# list와 공통점
# 1. 인덱싱 슬라이싱 가능
print(food[0])
print(food[0:2])

# 2. + 가능
food2 = ("만두", "와앙ㄴ")
food3 = food+food2
print(food3)

# list와 차이점
# 1. 값 변경 불가
# food[0] = "김치"
# print(food)