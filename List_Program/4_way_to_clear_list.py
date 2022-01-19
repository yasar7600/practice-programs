#1.
#  Python program to clear a list
# using clear() method

# Creating list
GEEK = [6, 0, 4, 1]
print('GEEK before clear:', GEEK)

# Clearing list
GEEK.clear()
print('GEEK after clear:', GEEK)




#2.
#  Python3 code to demonstrate
# clearing a list using
# clear and Reinitializing

# Initializing lists
list1 = [1, 2, 3]
list2 = [5, 6, 7]

# Printing list1 before deleting
print ("List1 before deleting is : "
+ str(list1))

# deleting list using clear()
list1.clear()

# Printing list1 after clearing
print ("List1 after clearing using clear() : "
+ str(list1))

# Printing list2 before deleting
print ("List2 before deleting is : "
+ str(list2))

# deleting list using reinitialization
list2 = []

# Printing list2 after reinitialization
print ("List2 after clearing using reinitialization : "
+ str(list2))





#3
#  Python3 code to demonstrate
# clearing a list using
# *= 0 method

# Initializing lists
list1 = [1, 2, 3]

# Printing list1 before deleting
print ("List1 before deleting is : " + str(list1))

# deleting list using *= 0
list1 *= 0

# Printing list1 after *= 0
print ("List1 after clearing using *= 0: " + str(list1))






#4
#    Python3 code to demonstrate
# clearing a list using
# del method

# Initializing lists
list1 = [1, 2, 3]
list2 = [5, 6, 7]

# Printing list1 before deleting
print ("List1 before deleting is : " + str(list1))

# deleting list1 using del
del list1[:]
print ("List1 after clearing using del : " + str(list1))


# Printing list2 before deleting
print ("List2 before deleting is : " + str(list2))

# deleting list using del
del list2[:]
print ("List2 after clearing using del : " + str(list2))

