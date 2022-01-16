#To find simple intrest rate
# Formula =(P*T*R)/100
# P is principal amount
# T is unit of Time
# R is rate
P = float(input("Enter principal of Amount :- "))
T = float(input("Enter Month of Time :- "))
R = float(input("Enter Rate of Intrest :- "))


def simple_intrest(P,T,R):
    I = (P*T*R)/100
    return I

print('Intrest is :-',simple_intrest(P,T,R))

