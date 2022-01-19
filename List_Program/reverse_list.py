mylist = [1,2,3,4,5,6,7,8,9]


#1
#def reverselist(ls):
#    ls.reverse()
#    return ls

#print(reverselist(mylist))


#2
def reverselist1(ls):
    new_list = []
    for i in reversed(ls):
        new_list.append(i)
    return new_list
print(reverselist1(mylist))



#3
def reverselist2(ls):
    new_list = ls[::-1]
    return new_list
print(reverselist2(mylist))
        