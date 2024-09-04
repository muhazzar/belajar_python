#mengambil data dari list
data=["apel","ular","bakwan"]
data_0=data[0]
print(f"data_1 index_0 = {data_0}")

data_akhir=data[-1]
print(f"data terakhir = {data_akhir}")

#mengambil info jumlah data
jumlah=len(data)
print(f"jumlah data di dalam list = {jumlah}")

#menambah item pada list sesuai posisi
data.insert(2,"kurma")
print(data)

#menambah item di posisi akhir
data.append("oren")
print(data)

#menggabungkan list
data_baru=("pdi","pks","pkb")
data.extend(data_baru)
print(data)

#merubah data
data[5]='merah'
print(data)

#remove data
data.remove("pks")
print(data)

#remove data terakhir
data.pop()
print(data)