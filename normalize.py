import numpy as np
import sys

'''
Normalize the data in foo.csv --> foo_normalized.csv

i.e...

Let A be an m x n matrix of features. The following code generates 
a file containing the matrix A', defined to be the matrix who's 
(i,j)^th element is equal to [A_ij - Avg(A_j)] / std_dev(A_j)]. 
Where Avg(A_j) and std_dev(A_j) are the column-wise average & 
standard deviation of the jth column of A respectivley.
'''

def normalize(filename):
    data = np.loadtxt(open(filename,"rb"), delimiter=",")
        
    avg0 = np.mean(data[:, 0])
    std0 = np.std(data[:,0])
    avg1 = np.mean(data[:,1])
    std1 = np.std(data[:,1])
    
    for i in range(0, len(data[:,0])):
        data[i,0] -= avg0
        data[i,0] /= std0
        data[i,1] -= avg1
        data[i,1] /= std1

    np.savetxt("{}_normalized.csv".
               format(filename.split('.')[0]), data, delimiter=",")
        
def main():
    if(len(sys.argv) == 1):
        print "ERROR: Please provide a filename!"
        exit(1)
        
    filename = sys.argv[1]
    normalize(filename)

    
if(__name__ == "__main__"):
    main()
