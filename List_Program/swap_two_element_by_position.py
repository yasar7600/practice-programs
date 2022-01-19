#swap two position by given position

def swapTwoElements(newlist, pose1, pose2):
    newlist[pose1],newlist[pose2] = newlist[pose2], newlist[pose1]
    return newlist


newlist = [12,34,54,67,45]

print(swapTwoElements(newlist, 0, 3))