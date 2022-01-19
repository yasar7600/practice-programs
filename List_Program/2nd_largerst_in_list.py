
ls = [10,20,5,30,50]

#1. using sort
#ls.sort()
#print(ls[-2])


#2. using max
#newls = set(ls)
#newls.remove(max(newls))
#print(max(newls))


#3. by user input using max

num = int(input("Enter Number of List Count:- "))

newls = []
for i in range(1, num +1):
    ele = int(input())
    newls.append(ele)
    
print("minimum number in list is :- ", sorted(newls)[-2])






