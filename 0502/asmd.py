#두 수를 입력받아 사칙연산 결과를 출력하는 프로그램

num1=int(input("첫 번째 정수 입력해주세요:"))

num2=int(input("두 번째 정수 입력해주세요:"))

print("{:2d} + {:2d}= {:3d}".format(num1,num2,(num1+num2)))
print("{:2d} - {:2d}= {:3d}".format(num1,num2,(num1-num2)))
print("{:2d} * {:2d}= {:3d}".format(num1,num2,(num1*num2)))
print("{:2d} / {:2d}= {:3f}".format(num1,num2,(num1/num2)))
