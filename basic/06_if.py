today = "수요일"


# if문의 조건이 맞으면 elif문은 실행되지 않음

if today == "월요일":
    print("출근") #들여쓰기 주의
elif today == "일요일":
    print("쉬는날")
else:
    print("무슨 요일이지?")


# 숫자 타입
day = 30

if day < 30:
    print("월급날이 . .")
elif day == 30:
    print("월급날")
else:
    print("흐음냐")


# bolean 타입
pizza = True
hamburger = False

if pizza:
    print("피자")
elif hamburger:
    print("햄버거")
else:
    print("배고팡")


# 중첩 if문
age = 20

if age >= 18:
    if age < 30:
        print("청년")


# 위 중첩 if문과 동일한 결과
if 18 <= age < 30:
    print("청년")