list_0=[1,2]
list_1=[3,4]

list_2d=[list_0,list_1]
print(list_2d,"\n")


peserta_0=["munir",97,"laki-laki"]
peserta_1=["alif",21,"laki-laki"]
peserta_2=["puni",15,"perempuan"]

list_peserta=[peserta_0,peserta_1,peserta_2]

for peserta in list_peserta:
    print(f"nama   : {peserta[0]}")
    print(f"umur   : {peserta[1]}")
    print(f"gender : {peserta[2]}\n")