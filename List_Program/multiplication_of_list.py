

ls = [4,3,2]

#1. Using for loop
#def multiListEle(ls):
#    total = 1
#    for i in range(0,len(ls)):
#        total *= ls[i]
#    return total
#print(multiListEle(ls))


#2. Using numoy
#import numpy as np
#total = np.prod(ls)
#print(total)

#3.using math
#import math
#total = math.prod(ls)
#print(total)


#4 Using lambda 
from functools import reduce

total = reduce((lambda x,y : x*y),ls)

print(total)
