import math



# Recursive function for Question #1
# Implements recurrence established in Week 9 Tuesday lecture of t_2 = 1 and t_n >= 2t_(n-1)
def orders(size):
    # Base Case
    if size == 2:
        return 1
    
    return 2 * orders(size-1)


# Global variables for chained matrix multiplication
minNumMult = 0
P = [] # matrix size/dimensions will be initialized in the main function

def minMult(d): # d is list of matrix dimensions from 0 to n
    n = len(d)-1
    M = [] # initialize M and values of 0 will be used for all spaces till changed
    # template appended to M until matrix that can easily be indexed 1 to n rather than 0 to n-1 is created, trimmed later with helper function
    template = [0, 0, 0, 0, 0, 0]
    for i in range(len(template)):
        M.append([0, 0, 0, 0, 0, 0])
    
    
    # allows access to global variables
    global P
    global minNumMult
    
    # don't need to initialize the main diagonal as it is already set to 0
    for diag in range(1, n):    
        for i in range(1, n - diag+1): 
            j = i + diag
            temp = [] # infinity assigned to all values of k before those in range(i, j)
            for z in range(0, i):
                temp.append(math.inf)
        
            for k in range(i, j): 
                temp2 = M[i][k] + M[k+1][j] + d[i-1] * d[k] * d[j]
                temp.append(temp2)
            M[i][j] = min(temp) # min value for all k's added to matrix M
            P[i][j] = temp.index(min(temp)) # P[i][j] is the index of the min value in temp
            
    minNumMult = M[1][n]
    print("Matrix M")
    trimMatrix(M)
    # Question 3A
    printMatrix(M)

# helper method to trim matrices from indexed 1 to n to 0 to n-1, gets them to proper size n x n
def trimMatrix(A):
    A.pop(0)
    for i in range(0, len(A)):
        A[i].pop(0)
        
        
# helper method for cleanly printing matrices
def printMatrix(A):
    for i in range(0, len(A)):
        print(A[i])


def main():
    
    # sizes of n to be tested for question 2
    print("num of orders for size of matrices nxn for n goes from 2 to 14 inclusive by steps of 2:")
    print(orders(2))
    print(orders(4))
    print(orders(6))
    print(orders(8))
    print(orders(10))
    print(orders(12))
    print(orders(14))
    
    print("")
    
    # template uses 1 extra x so that it is easier to interpret them as being indexed from 1 to n rather than 0 to n-1
    # matrices trimmed down to proper formatting later
    Ptemplate = ["x", "x", "x", "x", "x", "x"]
    for i in range(0, len(Ptemplate)):
        P.append(["x", "x", "x", "x", "x", "x"])
    
    
    # initializing list d, matrix dimensions
    d = [10, 4, 5, 20, 2, 50]
    
    
    minMult(d)
    
    print("")
    print("Matrix P")
    trimMatrix(P)
    # Queston 3b
    printMatrix(P)
    print("")
    print("min number of multiplactions:")
    # Question 3c
    print(minNumMult)
    
    
    
    
    print("")
    print("main has run")

if __name__ == '__main__':
    main()