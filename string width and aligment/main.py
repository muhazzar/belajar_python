#string multiline menggunakan \n

print(r'enter,\n'.center(20,'='))
dataNama='puluPulu'
dataUmur=20
dataTinggi=120
print('nama :',dataNama,'\ntinggi :',dataTinggi,'\numur :',dataUmur)

#string multiline menggunakan ''''''

print('\n')
print('kutip triplets'.center(20,'='))

print(f'''nama :{dataNama}
umur :{dataTinggi}
tinggi:{dataUmur}
''')

#ngatur lebar

print('\n')
print('rata kanan'.center(20,'='))

print(f'''nama  :{dataNama:>8}
umur  :{dataTinggi:>8}
tinggi:{dataUmur:>8}
''')
