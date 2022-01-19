# sum of list

ls = [1,2,3,4,5,6,7,8,9,10]


#1. using for loop
def sumOfList(ls):
    total = 0
    for i in range(0,len(ls)):
        total = total + ls[i]
    return total
print(sumOfList(ls))

#2. using sum function
#def sumOfList(ls):
#    #total = 0
#    total = sum(ls)
#    return total

#print(sumOfList(ls))

#3. Using while loop
#def sumOfList(ls):
#    total = 0
#    ele = 0
#    while (ele< len(ls)):
#        total = total + ls[ele]
#        ele += 1
#    return total

#print(sumOfList(ls))