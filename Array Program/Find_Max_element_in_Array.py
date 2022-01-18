arr = [5,10,4553,34,23,5000,300]

n = len(arr)

def maxElement(arr,n):
    max = arr[0]
    for i in range(1,n):
        if max < arr[i]:
            max = arr[i]
    return max

print("Max Element Of Array is :- ", maxElement(arr, n))