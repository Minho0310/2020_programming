a=input("주민등록번호를 입력해주세요 ex.821010-1635210 : ")

b=int(a[0])*2 + int(a[1])*3 + int(a[2])*4 +int(a[3])*5 + int(a[4])*6 + int(a[5])*7 +int(a[6])*8 +int(a[7])*9 +int(a[8])*2 +int(a[9])*3 +int(a[10])*4 +int(a[11])*5
c=b%11
d=11-c

if d > 9:
    d=d-10
else:
    pass

if d== int(a[12]):
    print("맞습니다")
else:
    print("틀렸습니다.")

