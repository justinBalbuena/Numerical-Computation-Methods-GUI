import numpy as np


def hadamard_walsh(f, N):
    #x,y is an operational intermediate buffer
    x = f.copy()
    # Calculate the number of iterations (n = log2(N))
    n = int(np.log2(N))
    for j in range(0, n):
        for k in range(0,pow(2,n-1)):
            #does the actions in the slide
            m = k+pow(2,n-1)
            x[2*k] = f[k]+f[m]
            x[2*k+1] = f[k]-f[m]
        #f.copy() to work with the new values after
        f = x.copy()
    return x
#from the slides with factorization(2') there are 2 different heads this is the one not provided I think
#this is from the algorithm provided in the slides
def hadamard_walsh_head_2(f,N):
    n = int(np.log2(N))
    x = f.copy()
    m = N
    for j in [1,n]:
        for r in range(1,pow(2,j-1)):
            s = 0
            for k in range(s,int(m/2)):
                x[k] = f[k]+f[int(k+m/2)]
            for k in range(int(m/2),N):
                x[k] = f[int(k-m/2)]-f[k]
            f = x.copy()
            m /= 2
            print(m)
            # f.copy() to work with the new values after

    return x


def main():
    signal = np.array([123,95,721,91,9,8,12,57])
    N = len(signal)
    if N % 2 != 0:
        print("Signal size must be a power of 2")
    else:
        solution = hadamard_walsh_head_2(signal,N)
        inverse = 1/N*hadamard_walsh_head_2(solution,N)
        print("\tSize 4","\noriginal vector: ",signal,"\nHadamard-walsh transform: ",solution,"\ninverse Hadamard walsh vector: ",inverse)
        #signal = np.array([123,95,721,91,9,8,12,57])
        # N = len(signal)
        # solution = hadamard_walsh_head_2(signal, N)
        # inverse = 1 / N * hadamard_walsh_head_2(solution, N)
        # print("\tSize 8","\noriginal vector: ", signal, "\nHadamard-walsh transform: ", solution, "\ninverse Hadamard walsh vector: ",inverse)
        # signal = np.array([123,95,721,91,9,8,12,57,123,95,721,91,9,8,12,57])
        # N = len(signal)
        # solution = hadamard_walsh_head_2(signal, N)
        # inverse = 1 / N * hadamard_walsh_head_2(solution, N)
        # print("\tSize 16","\noriginal vector: ", signal, "\nHadamard-walsh transform: ", solution, "\ninverse Hadamard walsh vector: ",inverse)
main()
