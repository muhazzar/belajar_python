
data_list=["bad thing","bad blood","liwet"]
data_copy=data_list.copy()

print(f"asli: {data_list}")
print(f"copy: {data_copy}\n")

data_copy[2]="migraine"#data asli tidak akan berubah

print(f"asli: {data_list}")
print(f"copy: {data_copy}")