#mengambil data dari list
data=["apel","ular","bakwan"]
print("data ori:",data)

data_0=data[0]
print(f"data 1 index 0: {data_0}")

data_akhir=data[-1]
print(f"data terakhir: {data_akhir}")

#mengambil info jumlah data
jumlah=len(data)
print(f"jumlah data di dalam list: {jumlah}")

#menambah item pada list sesuai posisi
data.insert(2,"kurma")
print(f"nambah kurma di index 2: {data}")

#menambah item di posisi akhir
data.append("oren")
print(f"nambah oren di akhir: {data}")

#menggabungkan list
data_baru=["pdi","pks","pkb"]
print("data baru:",data_baru)

data.extend(data_baru)
print("menggabungkan data dengan data_baru:",data)

#merubah data
data[5]='merah'
print("mengubah item index 5:",data)

#remove data
data.remove("pks")
print("menghapus item 'pks:",data)

#remove data terakhir
data.pop()
print("menghapus item terakhir:",data)