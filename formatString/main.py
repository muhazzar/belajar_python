#format string
nama="kunpay"
formatStr=f"nama {nama}"
print(formatStr)

#format angka
num=1235.5
format=f'number = {num}'
print(format)

ribu=300000
format=f'ribuan = {ribu:,}'
print(format)

desi=145145.1451245
format=f"desimal = {desi:.2f}"
print(format)
format=f"desimal = {desi:011.2f}"
print(format)

minus=-2
plus=2
formin=f'minus = {minus:+d}'
forplus=f'plus = {plus:+d}'
print(formin)
print(forplus)

persen=12.23
format=f'persen = {persen:.2%}'
print(format)

harga=20000
jumlah=2
format=f'total = {harga*jumlah:,}'
print(format)

num=255
formatBin=f'binary = {bin(num)}'
formatOctal=f'octal = {oct(num)}'
formatHex=f'hexadecimal = {hex(num)}'
print(formatBin)
print(formatOctal)
print(formatHex)