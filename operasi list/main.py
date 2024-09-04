numbers=[1,2,5,4,3,4,6,2,5,7,5,6,9,7,5]

#data count
seven=numbers.count(7)
print(f"jumlah angka 7 = {seven}")

five=numbers.count(5)
print(f"jumlah angka 5 = {five}")

#ambil posisi data {index}
data=["jeruk","bohlam","paiz","koi"]
print(data)

index_paiz=data.index("paiz")
print(f"index paiz = {index_paiz}")

index_jeruk=data.index("jeruk")
print(f"index jeruk = {index_jeruk}")

#mengurutkan data
print(f"before sort : {numbers}")
numbers.sort()
print(f"after sort : {numbers}")

print(f"before sort : {data}")
data.sort()
print(f"after sort : {data}")

#baliklist
numbers.reverse()
data.reverse()
print(f"reverse : \n{numbers}\n{data}")