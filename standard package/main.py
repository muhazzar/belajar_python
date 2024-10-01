import datetime

data_waktu=datetime.datetime.now()
print(f"now: {data_waktu}")
print(f"tahun: {data_waktu.year}")
print(f"hari: {data_waktu.strftime('%A')}")

from collections import Counter

data=['A','A','A','A','B','C','C','B','D','A','D','D']
data_count=Counter(data)
print(data_count)
print(f"jumlah A: {data_count['A']}")
print(f"jumlah B: {data_count['B']}")
print(f"jumlah C: {data_count['C']}")
print(f"jumlah D: {data_count['D']}")

