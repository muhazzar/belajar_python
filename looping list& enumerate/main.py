#for loop

print("forloop\n".center(20))

peserta=["ojak","denis","manuk","ropi"]

for nama in peserta:
    print(f"nama : {nama}")


#for loop & range

print("\nforloop & range\n".center(20))

kumpulan_angka=[1,2,3,4,5] 

panjang=len(kumpulan_angka)

for i in range (panjang):
    print(f"angka = {kumpulan_angka[i]}")

#while loop

print("\nwhile\n".center(20))

kumpulan_angka=[2,4,3,5]
panjang=len(kumpulan_angka)
i=0
while i < panjang:
    print(f"anngka = {kumpulan_angka[i]}")
    i+=1

#list comprehension

print("\nlist comprehension\n")

data_list=["jeruk",2,3,"monas"]

[print(f"data = {i}")for i in data_list]

#enumerate

print("\nenumerate\n")

for index,data in enumerate (data_list):
    print(f"index = {index},data = {data}")