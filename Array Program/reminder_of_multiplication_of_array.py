##Python Program for Find remainder of array multiplication divided by n

arr=[100,10,5,25,35,14]

def reminderofarraymulti(arr,d):
    multi = 1
    for i in arr:
        multi = multi * i
    rem = multi % d
    return rem

print(reminderofarraymulti(arr, 11))
    

#from functools import reduce

#def find_remainder(arr,n):
#    #use the reduce function to calculate sum

#   sum_1=reduce(lambda x,y: x*y,arr)

#   remainder=sum_1%n

#   print(remainder)

#arr=[14,24,45]

#n=11

#find_remainder(arr,n)

