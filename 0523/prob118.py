a=input("종목명은? : ")
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

if a in warn_investment_list:
    print("투자경고 종목입니다")
else:
    print("투자경고 종목이 아닙니다")
