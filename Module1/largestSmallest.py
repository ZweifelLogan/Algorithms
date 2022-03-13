
def findLargest(L):
    maximum = L[0]
    i = 0
    for i in range(0, len(L)-1):
        if L[i] > maximum:
            maximum = L[i]
    return maximum

def findSmallest(L):
    minimum = L[0]
    i = 0
    for i in range(0, len(L)-1):
        if L[i] < minimum:
            minimum = L[i]
    return minimum

def findLargestSmallest(L):
    maximum = L[0]
    minimum = L[0]
    i = 0
    for i in range(0, len(L)-1):
        if L[i] > maximum:
            maximum = L[i]
        elif L[i] < minimum:
            minimum = L[i]
    return (maximum, minimum)
    