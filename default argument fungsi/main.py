def say_hello(nama = 'gecko'):
    print(f'hai {nama}')

say_hello('oscar')
say_hello()
 


def sayHI(nama,pesan="apa kabar?"):
    print (f"hai {nama},{pesan}")

sayHI('stallin','apakah kamu manusia')
sayHI('yunus')



def hitung_pangkat(angka,pangkat):
    hasil=angka**pangkat
    return hasil
a=hitung_pangkat(2,4)
print(a)