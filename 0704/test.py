city=["부산","대구","대전"]
for a in range(len(city)):
    print(city[a])
city.insert(0,"서울")
city.insert(3,"인천")
print(city)
del city[3]
city.insert(3,"울산")
del city[1:3]
