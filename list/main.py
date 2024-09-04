#RANGE
data_range=range(0,10)
print(data_range)
data_list=list(data_range)
print(data_list)

#FOR
data_for=[i**3 for i in range(0,10)]
print(data_for)

#FOR,IF
forif=[i for i in range(0,10)if i !=5]
print(forif)

genap=[i for i in range (0,10)if i %2 ==0]
print(genap)

ganjel=[i for i in range(0,10)if i%2 !=0]
print(ganjel)