food = [1,2,3]

print(food[0:2])

# 숫자형 , 문자형 혼합 가능
food = [1, "햄버거"]

# 중첩 리스트?
food = [1,2, ["햄버거", "피자"]]

# 메소드
food = ["김치", "삼겹살"]

food.append("피자")
print(food)


# insert
food.insert(1, "햄버거")
print(food)

# remove 처음 하나만 삭제
food.remove("김치")
print(food)

# count
print(food.count("김치"))

# index
print(food.index("삼겹살"))

# sort
# 오름차순 정렬
food.sort()
print(food)

# 내림차순 정렬
food.sort(reverse=True)
print(food)