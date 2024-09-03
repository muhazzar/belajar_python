sisi=6

# menggunakan for

count=1
for i in range(sisi) :
    print("*"*count)
    count += 1

# menggunakan while

count=1
while True:
    print("*"*count)
    count+=1

    if count > sisi:
        break

# ganjel

count=1
while True:
    if count%2:
        print("*"*count)
        count+=1

    else:
        count+=1
        continue

    if count > sisi:
        break

# sama sisi
count=1
spasi=int(sisi/2)
while True:
    if count%2:
        print(" "*spasi,"0"*count)
        count+=1
        spasi-=1
    else:
        count+=1
        continue
    if count >sisi:
        break

        