
#사용자로부터 정수를 입력받아 1부터 입력한 정수까지의 합을 구하는 프로그램
s=0
a=int(input("정수입력:"))
b=range(1,a+1)
for i in b:
    s=s+i
print("1부터",a,"까지의 합=",s)
    
