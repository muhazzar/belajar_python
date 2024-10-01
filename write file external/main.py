# "w" /write: nimpa 

with open ("data_1.txt","w",encoding="utf-8") as file:
    file.write("jhon ling ling") 

with open("data_1.txt","w",encoding="utf-8")as file:
    file.write("chaonima")

# "a" /append: nambah
with open("data_2.txt","w",encoding="utf-8")as file:
    file.write("jhon ling ling\n")

with open("data_2.txt","a",encoding="utf-8")as file:
    file.write("ding dong")