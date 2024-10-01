from math import nan

#input_user=int(input("masukan angka:"))
#hasil=nan

#try:
#    hasil=10/input_user
#except:
#    print("masukan angka lain")
#print(hasil)


while (True):
    angka=int(input("masukan angka: "))
    try :
        hasil=10/angka
        print(f"hasil={hasil}")
        is_done=input("lanjutkan (y/n)?")
        if is_done=="n":
            break
    except:
        print("pembagi 0, masukan angka lain")
print("akhir program 1")


while(True):
    try:
        with open("data.txt","r")as file:
            print(file)
            break
    except:
        print("file tidak ditemukan,membuat file baru")
        with open("data.txt","w",encoding="utf-8")as file:
            file.write("file baru yoi")
            break
print("akhir program 2")