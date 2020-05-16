#원의 면적을 구하는 프로그램을 작성하시오,
#원의 면적 = 높이*밑변
import math

radius=int(input('반지름 입력: '))

area=math.pi *(radius**2)

print('반지름은',radius,'원의 면적은',area,'입니다')
