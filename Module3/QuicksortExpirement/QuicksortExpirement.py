import random
import math
import timeit

#! Deterministic Quicksort

def quicksort(S, low, high):
    if low < high:
        
        part = partition(S, low, high)
        quicksort(S, low, part-1)
        quicksort(S, part+1, high)


#! Partition for deterministic quicksort

def partition(S, low, high):
    pivotItem = S[low]
    j = low
    for i in range(low+1, high):
        if (S[i] < pivotItem):
            j = j+1
            S[i], S[j] = S[j], S[i]
    pivotPoint = j
    S[low], S[pivotPoint] = S[pivotPoint], S[low]
    return pivotPoint
  
    
        
    


#! Randomized quicksort
# the exact same as deterministic quicksort, the change is in partition

def randQuicksort(S, low, high):
    if low < high:
        
        part = randPartition(S, low, high)
        randQuicksort(S, low, part-1)
        randQuicksort(S, part + 1, high)

 

#! partition for randomized quicksort

def randPartition(S, low, high):
    r = random.randint(low, high)
    S[low], S[r] = S[r], S[low]
    
    pivotItem = S[low]
    j = low
    for i in range(low+1, high):
        if (S[i] < pivotItem):
            j = j+1
            S[i], S[j] = S[j], S[i]
    pivotPoint = j
    S[low], S[pivotPoint] = S[pivotPoint], S[low]
    return pivotPoint





#!
#! These two quicksorts are almost correct, they seem to leave one or two elements unsorted though. Don't think
#! it will be hard to find why.


def main():
    
    # TODO: delete out this test code
    # Deterministic quickSort
    list = [3, 10, 7, 8, 9, 1, 5, 2, 4, 6]
    len_list = len(list)
    quicksort(list, 0, len_list-1)
    #for i in range(len_list):
    #    print("%d" % list[i])
    print(list)
    print("")
    
    # randomized quicksort
    list2 = [3, 10, 7, 8, 9, 1, 5, 2, 4, 6]
    len_list2 = len(list2)
    randQuicksort(list2, 0, len_list2-1)
    print(list2)
    print("")
    # TODO: Testing code ends here
    
    maxSize = 10000
    
    
    #TODO: still need to implement the code for timing the algs
    # loop to run test for all sizes
    for i in range(1000, maxSize+1, 10000):
        
        # current size
        size = i
        
        # loop used to get run trial with same size to get a more accurate average measurement
        temp = 0
        for temp in range(0, 11):
            
            # List used for first question, sequence n, n-1, n-2, ..., 1
            List1 = []
            
            count = 0
            for count in range(size):
                temp2 = size-count
                List1.append(temp2)
            
            quicksort(List1, 0, len(List1)-1)
            randQuicksort(List1, 0, len(List1)-1)
            
            
            # List used for the second question - almost sorted list
            
            List2 = []
            
            count2 = 0
            for count2 in range(size):
                temp3 = count2 +1
                List2.append(temp3)
            
            # swaps 10 random elements in List2
            for x in range(0, 11):
                y = random.randint(0, size-1)
                z = random.randint(0, size-1)
                List2[z], List2[y] = List2[y], List2[z]
            
             
            quicksort(List2, 0, len(List2)-1)
            randQuicksort(List2, 0, len(List2)-1)
            
            
            # List used for third question - random permutation
            
            # first make a list like one used in question two, then randomly remove elements and append them to List3
            
            tempList = []
            
            count3 = 0
            for count3 in range(size):
                temp4 = count3 + 1
                tempList.append(temp4)
            
            # randomly remove fomr tempList and append to List3
            
            List3 = []
            
            for count4 in range(size):
                index = random.randint(0, len(tempList)-1)
                item = tempList[index]
                List3.append(item)
                tempList.pop(index)
            
            quicksort(List3, 0, len(List3)-1)
            randQuicksort(List3, 0, len(List3)-1)
                
                
            
                
        
    
    
    
    print("Main has run")



if __name__ == '__main__':
    main()