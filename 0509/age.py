import datetime
name=input('이름 입력: ')
year = int( input('출생연도 입력: '))
now = datetime.datetime.now()
age = now.year - year+1
print(name,'님의 나이는',age,'입니다')
