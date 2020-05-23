a=input("전화번호를 입력해주세요 ex.01012345678 : ")
b=a[0:3]
if b=="011":
    print("당신은 skt사용자입니다.")
elif b=="016":
    print("당신은 kt사용자입니다.")
elif b=="019":
    print("당신은 LGU사용자입니다.")
elif b=="010":
    print("알수 없음.")

