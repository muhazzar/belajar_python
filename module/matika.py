def tambah(*args):
    output=0
    for angka in args:
        output += angka
    return output


def kali(*args):
    output=1
    for angka in args:
        output *= angka
    return output


def pangkat(n:int):
    return lambda angka:angka**n

