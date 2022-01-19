#check the given array is monotonic or not

def Monotinic(A):

    return (all(A[i]<=A[i+1] for i in range(len(A)-1)) or
    all(A[i]>=A[i+1] for i in range(len(A)-1)))

A = [6,5,7,3]

print(Monotinic(A))