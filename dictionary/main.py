#dictionary

data_dict={
    "sg":"signature",
    "mg":"magnum",
    "sm":"samsu"
}
print(f"DATA AWAL: {data_dict}\n")

#panjang dictionary
lendict=len(data_dict)
print(f"panjang dictionary: {lendict}\n")

#ngecek key exist
key="mg"
checkey=key in data_dict
print(f"key 'mg' di data_dict: {checkey}\n")

#mengakses value (read) dengan get
print(data_dict.get("mg"))
print(data_dict.get("gr"))


#mengupdate data
print("\nUPDATE1")
data_dict["sm"]="sampoerna"
print(data_dict)
data_dict["gr"]="garpit"
print(data_dict)


print("\nUPDATE2")
data_dict.update({"sm":"samsu"})
print(data_dict)
data_dict.update({"pm":"philipmorris"})
print(data_dict)

#delete data
print("\nDELETE")
del data_dict["pm"]
print(data_dict)