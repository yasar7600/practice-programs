num = int(input("Enter NUmber:- "))

c=0
a=1
b=1

if num == 0 or num == 1:
    print("Yes It's In Fibbonaci")
else:
    while c<num:
        c = a + b
        b = a
        a = c
    if c == num :
        print("Yes It's In Fibbonaci")
    else:
        print("No It's Not In Fibbonaci")
