#kuadrat fungsi 
def fungsi_kuadrat(angka):
    return angka**2
print(f"hasil fungsi**: {fungsi_kuadrat(2)}") 

#kuadrat lambda
kuadrat=lambda angka:angka**2
print(f"hasil lambda**: {kuadrat(3)}")

pangkat=lambda num,pow:num**pow
print(f"hasil lambda pangkat: {pangkat(4,2)}\n")


#sorting list biasa
data_list=["aminahmaemunah","biinah","ceu inah"]
data_list.sort()
print(f"sorted list biasa {data_list}\n")

#sorting list pake len
data_list.sort(key=len)
print(f"sorting list by len: {data_list}\n")

#sort pake lambda
data_list=["aminahmaemunah","biinah","ceu inah"]
data_list.sort(key=lambda nama:len (nama))
print(f"sort by lambda: {data_list}\n")


#filter
data_angka=[1,2,3,4,5,6,7,8,9]
data_filter=list(filter(lambda x:x <6,data_angka))
print (data_filter)


data_ganjil=list(filter(lambda x:(x%2!=0),data_angka))
print(data_ganjil)

data_genap=list(filter(lambda x:(x%2==0),data_angka))
print(data_genap)

#anonymous
def pangkat(n):
    return lambda angka:angka**2
pangkat2=pangkat(2)
print(f"pangkat2 = {pangkat2(5)}")