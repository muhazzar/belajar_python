#kalkulator sederhana

angka_pertama=float(input("angka pertama :"))
operator=input("operator :")
angka_kedua=float(input("angka kedua :"))

if operator=="+":
    print("hasil :",angka_pertama + angka_kedua)
elif operator=="-":
    print("hasil :",angka_pertama - angka_kedua)
elif operator=="x":
    print("hasil :",angka_pertama * angka_kedua)
elif operator=="/":
    print("hasil :",angka_pertama / angka_kedua )
else :
    print("ERROR")