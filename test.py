num = int(input("Enter Number:- "))

order = len(str(num))

temp = num
def armstrongnumber(num ,temp,order):
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** order
        temp = temp // 10
    if num == sum:
        print("number is Armstrong Number")
    else:
        print("NUmber is not Armstrong Number")
    return sum

armstrongnumber(num, temp, order)
