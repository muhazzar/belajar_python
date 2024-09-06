
list_buku=[]

while True:
    print("\nmasukan data Buku\n".center(20))
    judul=input("masukan judul buku :")
    penulis=input("masukan nama penulis :")
    buku_baru=(judul,penulis)
    list_buku.append (buku_baru)
    for index,buku in enumerate (list_buku):
        print(f"{index+1}\t{buku[0]}\t{buku[1]}")
    print(20*"=","\n")
    isnext=input("lanjut? (y/n)")
    if isnext =="n":
        break
print("\nSELESAI\n".center(20))