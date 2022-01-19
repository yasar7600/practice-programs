

def swapFLelement(newlist):
    size = len(newlist)
    temp = newlist[0]
    newlist[0] = newlist[size - 1]
    newlist[size - 1]= temp
    return newlist


newlist = [12,34,54,67,45]

print(swapFLelement(newlist))