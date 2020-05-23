import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

a=opening_price + (max_price - min_price)
b=max_price

if a>b:
    print("상승장")
else:
    print("하락장")
