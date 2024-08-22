#NOT
print('                         NOT')
a=True
b=not a
print("data a :",a)
print("data b :",b)

#OR(jika salahsatrue maka hasilnya true)
print('                         OR')
a=True
b=False
c=a or b
print(a,"or",b,"=",c)

a=False
b=True
c=a or b
print(a,"or",b,"=",c)

a=False
b=False
c=a or b
print(a,"or",b,"=",c)

#AND
print('                         AND')

a=True
b=False
c=a and b
print(a,"and",b,"=",c)

a=False
b=True
c=a and b
print(a,"and",b,"=",c)

a=True
b=True
c=a and b
print(a,"and",b,"=",c) 

#XOR
print('                         XOR')

a=True
b=False
c=a ^ b
print(a,"xor",b,"=",c)

a=False
b=True
c=a ^ b
print(a,"xor",b,"=",c)

a=True
b=True
c=a ^ b
print(a,"xor",b,"=",c) 

a=False
b=False
c=a ^ b
print(a,"xor",b,"=",c) 

print('                                  ')

inputUser=float(input('masukan angka lebih dari nol dan kurang dari lima :'))
kurdar=inputUser < 5
ledar=inputUser > 0
print('kurang dari 5:',kurdar)
print('lebih dari 0:',ledar)
correct=kurdar or ledar
print('angka yang di masukan :',correct)