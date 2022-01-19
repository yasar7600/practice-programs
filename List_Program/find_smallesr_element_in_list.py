
ls = [10,20,5,30,50]

#1. using sort
#ls.sort()
#print(ls[:1]) 
##or
#print(ls[0])


#2. using min
#newls = min(ls)
#print(newls)


#3. by user input using min

num = int(input("Enter Number of List Count:- "))

newls = []
for i in range(1, num +1):
    ele = int(input())
    newls.append(ele)
    
print("minimum number in list is :- ", min(newls))






