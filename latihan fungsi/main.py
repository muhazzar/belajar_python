
def header():
    import os
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PPERSEGI PANJANG':^40}")
    print("-"*40)


def input_user():
    panjang=int(input("masukan nilai panjang: "))
    lebar=int(input("masukan nilai lebar: "))
    return lebar,panjang


def hitung_luas(panjang,lebar):
    return panjang*lebar


def hitung_keliling(panjang,lebar):
    return 2*(panjang + lebar)


def display(massage,value):
    print(f"hasil perhitungan {massage} = {value}")


def pilihan():
    tanya_opsi=int(input('1 untuk menghitung luas,2 untuk menghitung keliling: '))



while True:
    header()

    PANJANG,LEBAR=input_user()

    opsi=input("ketik 1 untuk luas,2 untuk keliling: ")
    if opsi=='1':
        LUAS=hitung_luas(PANJANG,LEBAR)
        display("luas",LUAS)

    elif opsi=='2':
        KELILING=hitung_keliling(PANJANG,LEBAR)
        display("keliling",KELILING)




    #LUAS=hitung_luas(PANJANG,LEBAR)
    #KELILING=hitung_keliling(PANJANG,LEBAR)
    #display("luas",LUAS)
    #display("keliling",KELILING)

    isContinue=input("next (y/n)")
    if isContinue == "n":
        break