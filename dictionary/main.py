#dictionary

data_dict={
    "sg":"signature",
    "mg":"magnum",
    "sm":"samsu"
}
print(f"data awal: {data_dict}\n")

#panjang dictionary
lendict=len(data_dict)
print(f"panjang dictionary: {lendict}\n")

#ngecek key exist
key="mg"
checkey=key in data_dict
print(checkey)

#mengakses value (read)dengan get
print(data_dict.get("mg"))
print(data_dict.get("gr"))

#mengupdate data
data_dict["sm"]="sampoerna"
print(data_dict.get("sm"))
data_dict["gr"]="garpit"
print(data_dict)

data_dict.update({"sm":"samsu"})
print(data_dict)
data_dict.update({"pm":"philipmorris"})
print(data_dict)

#delete data
del data_dict["pm"]
print(data_dict)