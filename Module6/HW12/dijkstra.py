# dijkstra_Tester.py
from math import inf
from dijkstra import *



########################################################################33
# MY WORK BEGINS HERE, DONT TOUCH ANYTHING ABOVE ################

def dijkstra(W):
    D = []
    P = []
    
    return (D, P)

def getPath(P, i):
    shortPath = []
    
    return shortPath







######################################################################
####### ALL MY WORK ABOVE THIS POINT ############################

def main():
    errorCount = 0
    
    # Testing Dijkstra's SSSP
    W = getSampleGraph()
    D, P = dijkstra(W)
    expectedD = [0, 10, 9, 6, 17]
    expectedP = [0, 0, 3, 0, 1]
    
    if D != expectedD:
        errorCount += 1
        print('-'*40)
        print('Error in D')
        print(f'   Expected {expectedD}')
        print(f'        Got {D}')
              
    if P != expectedP:
        errorCount += 1
        print('-'*40)
        print('Error in P')
        print(f'   Expected {expectedP}')
        print(f'        Got {P}')
    # Testing reconstructing the shortest paths
    # Using the expected list P
    expected_paths = [[0], [0, 1], [0, 3, 2], [0, 3], [0, 1, 4]]
    
    n = len(W)
    for i in range(n):
        sp = getPath(P, i)
        if sp != expected_paths[i]:
            errorCount += 1
            print('-'*40)
            print(f'Error in SP to v{i}')
            print(f'   Expected {expected_paths[i]}')
            print(f'        Got {sp}')
            
    print('-'*40)
    if errorCount == 0:
        print('No Errors Found')
    else:
        print(f'{errorCount} Error(s) Found')
def getSampleGraph():
    # See the homework assignment for a picture of this graph.
    n = 5
    W = [[inf for i in range(n)] for j in range(n)]
    for i in range(n):
        W[i][i] = 0
    W[0][1] = 10
    W[0][3] = 6
    
    W[1][0] = 3
    W[1][2] = 16
    W[1][3] = 4
    W[1][4] = 7
    
    W[2][1] = 8
    W[3][2] = 3
    
    W[4][2] = 9
    W[4][3] = 6
    
    return W
main()
