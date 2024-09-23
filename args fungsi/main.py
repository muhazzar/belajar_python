def fungsi (*args):
    nama=args[0]
    tinggi=args[1]
    berat=args[2]
    print(f"{nama} memiliki tinggi {tinggi} dan berat {berat}")

fungsi('maman',200,70)


#gapake *args
def fungsi(list):
    nama=list[0]
    tinggi=list[1]
    berat=list[2]
    print(f"{nama} memiliki tinggi {tinggi} dan berat {berat}")

fungsi(['mamet',250,45])#pake kurung kotak



#kwargs
def fungsi(**kwargs):
    name=kwargs["name"]
    tinggi=kwargs["tinggi"]
    berat=kwargs["berat"]
    print(f"{name} memiliki tinggi {tinggi} dan berat {berat}")

fungsi(name="anin",tinggi=150,berat=70)