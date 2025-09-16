# 기본 구조 = {"key" : "value"}
user = {"name" : "berry", "job" : "qa", "email" : "ddd@ddd.com"}
print(user["name"])

# 추가
user["age"] = 25
print(user)

# 삭제
del user["age"]
print(user)

# dict > list 형 변환
keys_list = user.keys()
keys_list = list(keys_list)
print(keys_list)
print(type(keys_list))

# value()
value_list = tuple(user.values())
print(value_list)
print(type(value_list))

# item()
item_list = user.items()
print(type(item_list))
print(item_list)