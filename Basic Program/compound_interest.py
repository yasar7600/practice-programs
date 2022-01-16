#To find simple intrest rate
# Formula =(P*T*R)/100
# A is Total Payable amount
# P is principal amount
# T is unit of Time
# R is rate
# Compound Intrest
P = float(input("Enter principal of Amount :- "))
T = float(input("Enter Unit of Time :- "))
R = float(input("Enter Rate of Intrest :- "))


def Compound_Intrest(P,T,R):
    A = P * (pow((1+R/100),T))
    CI = A - P
    return CI

print('Compound Intrest is :- ',Compound_Intrest(P,T,R))
print('Payable Amount is :- ',Compound_Intrest(P,T,R) + P)

