
test_list = [34,54,64,75,63,45,24]
n = int(input("Enter Number for check:- "))

for i in test_list:
    if (n == i):
        print("Exist")


#using in
if (0 in test_list):
    print("Exist")
else:
    print("dosen't Exist")