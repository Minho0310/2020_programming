a=input("돈을 입력해주세요 ex.100달러,100 엔,100유로,100위안 : ")
b=int(a[:-2])
c=a[-2:]

if c =="달러":
      print(b*1167,"원")
elif c==" 엔":
    print(b*1.096,"원")

elif c=="유로":
    print(b*1268,"원")
elif c=="위안":
    print(b*171,"원")
