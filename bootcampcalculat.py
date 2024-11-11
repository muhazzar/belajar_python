def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"
    
def main():
    print("Kalkulator command line")
    print("operasi yang di dukung: +,-,*,/")

    while True:
        try:
            num1=float(input("masukan angka pertama: "))
            operator=input("masukan operator (+,-,*,/): ")
            num2=float(input("masukan angka kedua: "))

            if operator == '+':
                print("hasil", add(num1 + num2))
            if operator == '-':
                print("hasil", subtract(num1 - num2))
            if operator == '*':
                print ("hasil", multiply(num1 * num2))
            if operator == '/':
                print("hasil", divide(num1 / num2))
            else:
                print("operator tidak valid silahkan coba lagi")

        except ValueError:
            print("input tidak valid. silahkan masukan nilai numerik")
        except Exception as e:
            print("terjadi kesallahan",e)

        choice=input("apakah anda ingin melakukan perhitungan lain? (yes/no): ").lower()
        if choice != 'yes':
            print("keluar dari kalkulator")
            break

if __name__ =="__main__":
    main()