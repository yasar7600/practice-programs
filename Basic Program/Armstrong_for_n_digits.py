num = int(input("Enter NUmber:- "))

order = len(str(num))

temp = num

def armstrongnumber(num,temp,order):
   sum = 0
   while temp > 0:
      digit = temp % 10
      sum = sum + digit ** order
      temp = temp // 10
   if sum == num :
      print("number is armstrong number")
   else:
      print("number is NOT armstrong number")

armstrongnumber(num,temp,order)




















#num = int(input("Enter a number: "))

## Changed num variable to string, 
## and calculated the length (number of digits)
#order = len(str(num))

## initialize sum
#sum = 0

## find the sum of the cube of each digit
#temp = num #15
#while temp > 0:
#   digit = temp % 10 
#   sum =sum + digit ** order #27+125+ 1
#   temp = temp // 10 # 15, 1

## display the result
#if num == sum:
#   print(num,"is an Armstrong number")
#else:
#   print(num,"is not an Armstrong number")