a = int(input('Enter Number :- '))

#                      1
# def factorial(n):
#     if n < 0:
#         return 0
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         fact = 1
#         while(n > 1):
#             fact = fact * n
#             n = n - 1
#         return fact
# result = factorial(a)
# print('Factorial of number is {0}'.format(result))


#                     2
# def factorial(n):
#     return 1 if (n==0 or n==1) else n * factorial(n-1)

# result = factorial(a)
# print('factorial of number is {0}'.format(result))

#                   3
import math

def factorial(n):
    return(math.factorial(n))

result = factorial(a)
print('factorial of number is {0}'.format(result))