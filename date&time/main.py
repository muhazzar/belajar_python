import datetime as dt

print('masukan tanggal lahir')
tanggal=int(input('tanggal :'))
bulan=int(input('bulan \t:'))
tahun=int(input('tahun \t:'))

tanggal_lahir=dt.date(tahun,bulan,tanggal)
print(f'tanggal lahir :{tanggal_lahir}')
print(f'hari :{tanggal_lahir:%A}')

print('\n')
hari_ini=dt.date.today()
umur=hari_ini - tanggal_lahir
umur_tahun=umur.days//365
umur_bulan_sisa=(umur.days % 365) // 30
print(f'sekarang tanggal :{hari_ini}')
print(f'hari :{hari_ini:%A}')
print(f'umur :{umur_tahun}tahun,{umur_bulan_sisa}bulan')
