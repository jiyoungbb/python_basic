name = "berry"
job = "QA"
age = 29

# 숫자열 + 문자열 불가
# print("hi my name is " + name + " my job is " + job + " i'm " + age)

# 해결방법1 형변환
print("hi my name is " + name + " my job is " + job + " i'm " + str(age))

# 해결방법2 %s
print("hi my name is %s my job is %s i'm %s" %(name, job, age))

# 해결방법3 format
print("hi my name is {0} my job is {1} i'm {2}" .format(name, job, age))

# 해결방법4 fstring   << 주로 사용
print(f"hi my name is {name} my job is {job} i'm {age}")