
nama=input('who are you? ')

#program if indentation
if nama=='ijar' : 
    print('Wazzup')

#program if inline
if nama=="ijar" :print(f'halo {nama}')

#else statement
if nama=='ijar':
    print(f"YO",nama)

else :
    print("LOL")


#elif statement
passwrd=input("masukan password :")
if passwrd=='456258':#kondisi 1
             print('WELCOME CAPT')#aksi true 1

elif passwrd=='321':#kondisi 2
             print('WELCOME BRO')#aksi true 2

elif passwrd=='654':#kondisi 3
             print('WELCOME GEORGE')#aksi true 3
             
else:
             print('go sleep kid')#aksi false