## variable global scope

nama="stallin"#ini variable global

#akses variable global dalam fungsi
def fungsi():
    print(f"fungsi menampilkan {nama}")

fungsi()

#akses variable global dalam loop
for i in range(2):
    print(f"{nama} {i}")


## variable locaal scope
def fungsi1():
    nama_1="joseph"#ini variable local
    print(nama_1)

fungsi1()
 

#penggunaan akses variable
def ehlo():
    print(f"hai {nama}")

nama="marjuk"
ehlo()


#merubah variable global
angka=0
warna="ijo"

def ubah(angka_baru,warna_baru):
    global angka
    global warna
    angka=angka_baru
    warna=warna_baru

print(f"sebelum {angka,warna}")
ubah(100,"maroon")
print(f"sesudah {angka,warna}")