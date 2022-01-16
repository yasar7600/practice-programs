num = int(input("Enter Number:- "))

if num > 1:
    for i in range(2,int(num/2)+1):
        if (num%i) == 0:
            print("number is NOT prime")
        else:
            print("Number is Prime")
elif num == 2:
    print("Number is Prime")

else:
    print("number is Not Prime")