#method overloading is not supported in python directly. ex:- under the code
from multipledispatch import dispatch

@dispatch(int,int)
def area(length,breath):
    return length*breath

@dispatch(int)
def area(redius):
    return 3.14*redius*redius

a = area(2)
print(a)






## First product method.
## Takes two argument and print their
## product
#def product(a, b):
#	p = a * b
#	print(p)
	
## Second product method
## Takes three argument and print their
## product
#def product(a, b, c):
#	p = a * b*c
#	print(p)

## Uncommenting the below line shows an error	
## product(4, 5)

## This line will call the second product method
#product(4, 5, 5)

'''In the above code, we have defined two product method, but we can only use the second product method, as python does not support method overloading. We may define many methods of the same name and different arguments, but we can only use the latest defined method. Calling the other method will produce an error. Like here calling product(4, 5)    will produce an error as the latest defined product method takes three arguments. https://www.geeksforgeeks.org/python-method-overloading/'''



