import random
import math
import timeit

# n is the number of vertices in the graph
# count is the vertices the row for the adjacency matrix is being generated for
def generateGraph(n, count):
    row = [] # row of adjacency matrix to be returned
    prob = 0.9 # the probability that a given vertices will connect to another
    
    
    # loop to generate edges in a directed weighted graph
    for i in range(0, n):
        if count  == i: # W[i][i] = 0
            row.append(0)
        else: # if not W[i][i]
            temp = random.random()
            if temp <= prob: # randomly generated number falls in range to generate an edge between count vertice and i vertice
                row.append(random.randrange(1, n+6)) # size/weight of edge ranges from 1 to 5 of above the number of vertices (n+6) used because range is exclusive
            else: # randomly generated number falls in range where no edge exists, assigns infinity
                row.append(math.inf)
    return row
 
 
 
#! Don't think this function will be necessary because with a probability of an edge connecting of 90% it is almost certain that a tour will exist       
# W is the adjacency matrix that represents the graph generated in generateGrap and stored in graph variable in main method
# a is the row and b is the column to identify any index in all of adjacency graph W
# initial call to this functin is hasTour(graph, 0, size, [0])
# used vertices is the list of vertices that have already been used in testing a tour
def hasTour(W, a, b, usedVertices):
    result = False
    #paths = [] # a list of vertices who have paths of length size of W (number of vertices in graph)
    
    # Base case, when a path of length W has occured, check to see if final vertex in path connects back to vertex 1 (index 0 in W)
    #if len(usedVertices) == len(W):
    #    paths.append(usedVertices[-1])
        
    for i in range(a, b):
        for j in range(a, b):
            if inList(usedVertices, j) == False:
            
            
            
            
                #print(W[i][j], usedVertices)
                #print(shouldRun(W[i][j]))
                if shouldRun(W[i][j]) == True and inList(usedVertices, j) == False:
                #    print("if statement ran")
                    usedVertices.append(j)
                    temp = usedVertices
                    hasTour(W, temp)
                #print(" ")
    
    
    # check to see if final vertex in paths of length W connect back to vertex 0 to form a tour
    for x in range(1, len(usedVertices)):
        if shouldRun(W[x][0]) == True:
            result = True 
    
    print(usedVertices)
    return result
                


 
    
#! If has tour is not needed for this, this function isn't either    
# helper function to determine value of a given W[i][j]
# if value is infinity or 0 the value should not be run (return False) otherwise return True
def shouldRun(a):
    if a == 0 or a == math.inf:
        return False
    else:
        return True
    
#! if hasTour is not needed for this, the function isn't either
# helper function to determine if element is already in list (sequential search)
def inList(list, a):
    for i in range(0, len(list)):
        if list[i] == a:
            return True
    return False






def tsp(W):
    D = []
    for i in range(2, len(W)):
        D[i][{}] = W[i][1]
    for k in range(1, len(W)-2):
        print("hi")

def main():
    # list made up of lists within a list that represents the adjacency matrix W of the graph generated in generate graph
    graph = []
    
    row = 0 # row/vertice that needs to be created for the adjacency matrix
    size = 5 # number of vertices in the graph
    
    for x in range(0, size):
        temp = generateGraph(size, row)
        graph.append(temp)
        row += 1
    
    tour = hasTour(graph, 0, len(graph), [0])
    
    print(graph)
    print(" ")
    print(tour)
    print(" ")
    print("Main has run")
    

if __name__ == '__main__':
    main()