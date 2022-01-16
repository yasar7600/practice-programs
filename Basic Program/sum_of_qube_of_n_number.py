num = int(input("Enter number:- "))


def sumOfQube(n):
    sm = 0
    for i in range(1,n+1):
        sm =sm + (i*i*i)
    return sm

print(sumOfQube(num))