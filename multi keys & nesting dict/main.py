import datetime

mahasiwa1={
    'nama':'among',
    'nim':'1902501',
    'sks':100,
    'lahir':datetime.datetime(2004,7,17)
}

mahasiwa2={
    'nama':'munir',
    'nim':'1902502',
    'sks':130,
    'lahir':datetime.datetime(2003,5,7)
}

mahasiwa3={
    'nama':'tarno',
    'nim':'1902503',
    'sks':140,
    'lahir':datetime.datetime(2000,3,3)
}

data_mahasiwa={
    'MAH001':mahasiwa1,
    'MAH002':mahasiwa2,
    'MAH003':mahasiwa3
}

print(f"{'KEY':<8} {'Nama':<6} {'NIM':<8} {'SKS':<5} {'Lahir':<10}")
print("-"*40)

for mahasiwa in data_mahasiwa:
    KEY=mahasiwa

    NAMA=data_mahasiwa[KEY]['nama']
    NIM=data_mahasiwa[KEY]['nim']
    SKS=data_mahasiwa[KEY]['sks']
    LAHIR=data_mahasiwa[KEY]['lahir'].strftime("%x")
    print(f"{KEY:<8} {NAMA:<6} {NIM:<8} {SKS:<5} {LAHIR:<10}")