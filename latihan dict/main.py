import datetime
import os
import string
import random

mahasiwa_template={
    'nama':'nama',
    'nim':'00000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
}

data_mahasiwa={}

while True:
    os.system("cls")

    print(f"{'DATA MAHASIWA':^20}")
    print("-"*20)

    mahasiwa = dict.fromkeys(mahasiwa_template.keys())

    mahasiwa['nama'] = input("Nama Mahasiwa: ")
    mahasiwa['nim'] = input("Nim Mahasiwa: ")
    mahasiwa['sks_lulus'] = int(input('SKS Lulus: '))
    TAHUN=int(input("Tahun lahir (YYYY): "))
    BULAN=int(input("Bulan lahir (1-12): "))
    TANGGAL=int(input("Tanggal lahir (1-31): "))
    mahasiwa['lahir'] = datetime.datetime(TAHUN,BULAN,TANGGAL)
    


    KEY="".join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiwa.update({KEY:mahasiwa})

    print(f"\n{"KEY":<8} {"NAMA":<6} {"NIM":<8} {"SKS":<5} {"LAHIR":<10}")
    print("-"*40)

    for mahasiwa in data_mahasiwa:
        KEY=mahasiwa
        NAMA=data_mahasiwa[KEY]['nama']
        NIM=data_mahasiwa[KEY]['nim']
        SKS=data_mahasiwa[KEY]['sks_lulus']
        LAHIR=data_mahasiwa[KEY]['lahir'].strftime("%x")
        print(f"{KEY:<8} {NAMA:<6} {NIM:<8} {SKS:<5} {LAHIR:<10}")

    print("\n")
    udah=input("(y/n)")
    if udah == "n":
        break

print("\nBERES ANJAYY")