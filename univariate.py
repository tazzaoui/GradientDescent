import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as FuncAnimation
import sys

def compute_residual(coefs, data):
    squared_residual = 0
    for i in range(0,len(data)):
        hypothesis = coefs[0] + coefs[1] * data[i,0]
        squared_residual += (hypothesis - data[i,1]) ** 2
    residual = squared_residual / (2*len(data))
    return residual

# Update each coef according to the partial deriv. of the cost function
def update_coefs(coefs, data, alpha):
    hb = hm = 0
    for i in range(0, len(data)):
        hypothesis = (coefs[0] + coefs[1] * data[i,0]) - data[i,1]
        hb += hypothesis
        hm += hypothesis*data[i,0]
    hb *= alpha/len(data)
    hm *= alpha/len(data)
    return hb, hm

def plot_data(data, coefs,i):
    pts, line = plt.subplots()
    l, = line.plot(data[:,0], coefs[1] * data[:,0] + coefs[0], color='red')
    plt.scatter(data[:,0], data[:,1])
    plt.title("Hypothesis: Y = {}x + {}".format(coefs[1], coefs[0]))
    plt.show()
    
def main():
    if(len(sys.argv) != 2):
        print "ERROR: Please provide a dataset"
        exit()
    filename = sys.argv[1]
    data = np.loadtxt(open(filename,"rb"), delimiter=",")
    iter = 1500
    alpha = 0.001
    coefs = [0,0]
    for i in range(0,iter):
        print "Y = " + str(coefs[1]) + "x + " + str(coefs[0])
        print "Iteration: {}".format(i)
        print "Residual: {}".format(compute_residual(coefs, data))
        new_coefs = update_coefs(coefs, data, alpha)
        coefs[0] -= new_coefs[0]
        coefs[1] -= new_coefs[1]
    plot_data(data, coefs,i)
    
if __name__ == "__main__":
    main()
