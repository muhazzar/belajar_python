def kuadrat(x):
    output=x**2
    return output

y=kuadrat(2)
print(y)



def fungsi_tambah(number_1,number_2):
    return number_1 + number_2

a=fungsi_tambah(4,7)
print(a)
print("\n")


def ngitung(num_1,num_2):
    kali=num_1 * num_2
    bagi=num_1 / num_2
    kureng=num_1 - num_2
    tambah=num_1 + num_2
    return kali,bagi,kureng,tambah

a,b,c,d=ngitung(6,3)

print(f"hasil kali = {a}")
print(f"hasil bagi = {b}")
print(f"hasil kureng = {c}")
print(f"hasil tambah = {d}")