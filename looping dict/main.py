cigarete={
    "sm":"samsu",
    "jc":"jarcok",
    "mg":"magnum",
    "gt":"garpit"
}

for oi in cigarete:
    print(oi)#yang muncul hanya key saja

#iterables/operator untuk mengambil item
key=cigarete.keys()
print(key)

for key in cigarete.keys():
    print(key)



values=cigarete.values()
print(values)

for value in cigarete.values():
    print(value) 



items=cigarete.items()
print(items)

for item in cigarete.items():
    print(item)



for key,velue in cigarete.items():
    print(f"key : {key} | velue : {velue}")