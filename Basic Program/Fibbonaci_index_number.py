num = int(input("Enter Number:- "))

def Fibbonaci(n):
    if n <= 0:
        print("Incorrect Input")
    elif n == 1 :
        return 0
    elif n == 2 :
        return 1
    else:
        return Fibbonaci(n-1)+Fibbonaci(n-2)

print(Fibbonaci(num))