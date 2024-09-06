data_0=[1,2]
data_1=[3,4,5]

data_2d=[data_0,data_1,6]
print(data_2d)

data_2d_copy=data_2d.copy()

from copy import deepcopy

data_deep=deepcopy(data_2d)


#mengambil data dari nested list
a=data_2d[0][0]
print(a)


print(f"address asli : {hex(id(data_2d))}")
print(f"address copy : {hex(id(data_2d_copy))}")
print(f"address deep : {hex(id(data_deep[0][0]))}")


data_2d[1][1]=9
data_2d[2]=7
print("asli :",data_2d)
print("copy :",data_2d_copy)
print("deep :",data_deep)



print("address member 1".center(35).upper())
print(f"address member 1 asli : {hex(id(data_2d[0]))}")
print(f"address member 1 copy : {hex(id(data_2d_copy[0]))}")
print(f"address member 1 deep : {hex(id(data_deep[0]))}")

