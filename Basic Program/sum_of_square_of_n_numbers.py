num = int(input("Enter number:- "))


def sumSquare(n):
    sm = 0
    for i in range(1 , n+1):
        sm = sm + (i * i)
    return sm

print(sumSquare(num))

