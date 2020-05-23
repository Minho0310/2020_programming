a=input("입력해주세요 : ")
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

if a in fruit.keys():
    print("정답입니다")
else:
    print("오답입니다")
