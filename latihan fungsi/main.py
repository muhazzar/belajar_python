import os
os.system("cls")

#header program
print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
print("-"*40)

#mengambil input user
PANJANG=int(input('masukan nilai panjang:'))
LEBAR=int(input('masukan nilai lebar:'))

#progrm menghitung luas
luas=PANJANG*LEBAR
keliling=2*(PANJANG + LEBAR)

#menampilkan hasil
print(f"hasil perhitungan luas = {luas}")
print(f"hasil perhitungan keliling = {keliling}")