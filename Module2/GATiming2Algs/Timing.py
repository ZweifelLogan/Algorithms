import random
import math
import timeit

def seqsearch(S, key):
    location=0
    present = False
    #For counting the # of comparisons, to be returned
    count = 0
    
    while location < len(S) and not present:
        if S[location] == key:
            present = True
        else:
            location += 1
        count += 1
    
    return(count) 
    
def binsearch(S, key):
    first = 0
    last = len(S)-1
    present = False
    #For counting the # of comparisons, to be returned
    count = 0
    
    while first <= last and not present:
        midpoint = ((first + last)//2)
        #count + 1 for comparing the midpoint of the list to the key
        count += 1
        if S[midpoint] == key:
            present = True
        else:
            #count + 1 for comparing the key to the midpoint again to see if greater or lesser
            count += 1
            if key < S[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
        
    
    return(count)


def main():
    # n - maximum size lists can be
    maxSize = 10000
    
    
    #code to generate a list size n with integers ranging from 1 to 2n/3, key is randomly selected form the list
    # in the range the first number is the starting size list and the third is the size of the steps in between the starting size and max size
    for i in range(100, maxSize+1, 100):
        
        # current size of list (n) that these algs will run on
        size = i
        
        #Averages of the measurements taken for both algorithms
        seqTimeAvg = 0
        seqCompAvg = 0
        binTimeAvg = 0
        binCompAvg = 0
        
        
        # temp and the loop used to run algs 50 times for the same size n to get an avg performance
        temp = 0
        for temp in range(0, 50):
            
            List = []
            upper = math.floor((2*size)/3)
            
            count = 0
            for count in range(size):
                temp2 = random.randrange(1, upper+1)
                List.append(temp2)
            List.sort()
            keyIndex = random.randrange(0, size)
            key = List[keyIndex]
            
            #Still within this large for loop run both algs using the list generated and the key
            seqStart = timeit.default_timer()
            seqComparisons = seqsearch(List, key)
            seqTime = timeit.default_timer() - seqStart
            
            binStart = timeit.default_timer()
            binComparison = binsearch(List, key)
            binTime = timeit.default_timer() - binStart
            
            #Add the measurements to the averages for this size n
            seqTimeAvg += seqTime
            seqCompAvg += seqComparisons
            binTimeAvg += binTime
            binCompAvg += binComparison
            
        # Divide the averages by 50 to get the correct numbers
        seqTimeAvg = seqTimeAvg / 50
        seqCompAvg = seqCompAvg / 50
        binTimeAvg = binTimeAvg / 50
        binCompAvg = binCompAvg / 50
        
        # On output: first number is size of list tested, then it seqsearch average time and average number of comparisons followed by binsearch in the same order
        print("")
        print(size)
        print(seqTimeAvg)
        print(seqCompAvg)
        print(binTimeAvg)
        print(binCompAvg)
            
    print("Main has run")
              

if __name__ == '__main__':
    main()
    