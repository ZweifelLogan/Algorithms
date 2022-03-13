def msmallest(L, m):
    #initialize final list to be returned
    final = []
    
    #Loop through parameter L, m times
    count = 0
    for count in range(0, m):
        
        #Saves the minimum value and its index in L
        minimum = L[0]
        minIndex = 0
        i= 0
        
        #Finds the minimum in L
        for i in range(0, len(L)):
            if L[i] < minimum:
                minimum = L[i]
                minIndex = i
        
        #Put minimum into final and pops that value at specific index from L
        final.insert(count, minimum)
        L.pop(minIndex)
            
    #Appends values that were removed from L back to it so more tests can be run on the same list
    x = 0
    for x in range(0, len(final)):
        L.append(final[x])

    return final
