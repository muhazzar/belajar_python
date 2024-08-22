#menggabungkan string
awal='Monkey'
tengah='D'
akhir='Rojak'

nama_lengkap = awal +" "+ tengah +"'"+ akhir
print(nama_lengkap) 

#menghitung jumlah string 'len'
jumlahHuruf=len(nama_lengkap)
print('jumlah huruf dalam',nama_lengkap,'ada',jumlahHuruf)

#mengulang string
print('wk'*5)
print(2*'awok')

#mengecek komponen char atau string yg ada
d='D'
status=d in nama_lengkap
print('huruf',d,'di',nama_lengkap,':',status)

#indexing
print('index ke 3 dari',nama_lengkap,":",nama_lengkap[3])
print('index ke 0:5 dari',nama_lengkap,":",nama_lengkap[0:5])
print('index ke 0,2,4,6 dari',nama_lengkap,":",nama_lengkap[0:7:2])

#ngecek item paling kecil
print('item paling kecil dari',nama_lengkap,':',min (nama_lengkap))
#ngecek item paling besar
print('item paling besar dari',nama_lengkap,':',max (nama_lengkap))
 
#operator dalam bentuk method
jumlah=nama_lengkap.count('o')
print('jumlah o pada',nama_lengkap,':',jumlah)

#merubah smua huruf menjadi uppercase
up=nama_lengkap.upper()
print(up)

#merubah smua huruf menjadi uppercase
low=nama_lengkap.lower()
print(low)

#ngecek lower/upper
lowkah=nama_lengkap.islower()
print('apakah huruf dalam',nama_lengkap,'lowcase :',lowkah)

upkah=nama_lengkap.isupper()
print('apakah huruf dalam',nama_lengkap,'upcase :',upkah)

#isalpha() buat cek apakah semuanya huruf
a="abcdefg"
cek=a.isalpha()
print('apakah komponen dari',a,'huruf semua :',cek)

#isalnum() cek huruf dan angka
passw='muh234'
cek=passw.isalnum()
print('apakah komponen dari',passw,'terdiri dari huruf dan angka :',cek )

#isdecimal() cek angka
num='12345'
cek=num.isdecimal()
print("apakah komponen dari",num,'angka semua :',cek)

#isspace() cek spasi,tab,newline
nam='\n\t'
cek=nam.isspace()
print(cek)

#istile() semua kata diawali huruf besar
man='Iron Man'
cek=man.istitle()
print(cek) 