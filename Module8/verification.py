
def verifyVertexCover(W, k, guessedSol): # W -> adjacency matrix, k -> integer, guessedSol -> guessed solution
    #1) |guessedSol| <= k must be TRUE
    if len(guessedSol) > k:
        return False
    
    #2) for all vertices in guessedSol, they must be between or equal to 1 and |W|
    for x in range(0,len(guessedSol)):
        if ((0 <= guessedSol[x] <= len(W)-1) == False):
            return False
    
    #3) Verify cover exists for vertices in guessedSol        
    for i in range(0, len(W)):
        for j in range(0, len(W)):
            if W[i][j] == 1:
              if i not in guessedSol and j not in guessedSol:
                  return False
    
    
    # If all checks are passed return True 
    return True

def verifyGraphColoring(W, m, guessedSol): #Inputs same as above verifyVertexCover
    #1) Verify length of solution same as number of vertices in graph 
    if len(guessedSol) != len(W):
        return False
    
    #2) Number of colors between 1 and number of vertices in G
    for x in range(0, len(guessedSol)):
        if (0 <= guessedSol[x] <= len(W)-1) == False:
            return False
      
    #3) For each W[i][j] == 1, check S[i] != S[j] 
    for i in range(0, len(W)):
        for j in range(0, len(W)):
            if W[i][j] == 1:
                if guessedSol[i] == guessedSol[j]:
                    return False
    
    # If all other checks pass return True
    return True
