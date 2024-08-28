#casting tipe data

#INTEGER
print("\n","INT".center(25,"="))
data_int  =9

data_float=float(data_int)
data_str  =str(data_int)
data_bool =bool(data_int)

print("data :" ,data_int,type(data_int)) 
print("data :" ,data_float,type(data_float))
print("data :" ,data_str,type(data_str))
print("data :" ,data_bool,type(data_bool))

#FLOAT
print("\n","FLOAT".center(25,"="))
data_float=9.9

data_int  =int(data_float)
data_str  =str(data_float)
data_bool =bool(data_float)

print("data :" ,data_int,type(data_int)) 
print("data :" ,data_float,type(data_float))
print("data :" ,data_str,type(data_str))
print("data :" ,data_bool,type(data_bool))

#STRING
print("\n","STRING".center(25,"="))
data_str="1"

data_int    =int(data_str)
data_float  =float(data_str)
data_bool   =bool(data_str)

print("data :" ,data_int,type(data_int)) 
print("data :" ,data_float,type(data_float))
print("data :" ,data_str,type(data_str))
print("data :" ,data_bool,type(data_bool))

#BOOLEAN
print("\n","BOOLEAN".center(25,"="))
data_bool=False

data_int    =int(data_bool)
data_float  =float(data_bool)
data_str   =str(data_bool)

print("data :" ,data_int,type(data_int)) 
print("data :" ,data_float,type(data_float))
print("data :" ,data_str,type(data_str))
print("data :" ,data_bool,type(data_bool))
