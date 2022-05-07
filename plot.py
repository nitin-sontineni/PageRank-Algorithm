import random
from Pagerank import powerIteration
from Pagerank import directMethod
from stochasticMatrix import generateMatrix
from matplotlib import pyplot as plt
from time import time

def main():
    """Driver code for calculating the required principle left eigen vectors
    """
    nedges = []
    powiter = []
    directiter = []
    totiter = []
    for i in range(2,1001):
        if i%50 == 0:
            print(i)
        names_website = [x for x in range(1,i)]
        edges = []
        for x in range(1,i):
            edges.append((x,x+1))
            edges.append((x+1,x))
        # print('Enter number of website links in the sample internet :-')
        n = i
        # if n == 0:
        #     print("Number of nodes should be greater than equal to one \n")
        #     return 
        # print('\n')
        # print('Enter the names of the website links :-')
        # for _ in range(n):
        #     names_website.append(input())
        # print('\n')
        # for i in range(n):
        #     print(str(i+1) + '->'+names_website[i])
        # print('\n')
        # print('Enter total number of edges in the directed graph:- ')
        m = len(edges)
        # print('The edges are:- ')
        # for _ in range(m):
        #     edges.append(tuple(map(int,input().split(","))))
        L = generateMatrix(edges,n,m)
        # print('\n')
        start = time()
        str(powerIteration(L,0.9))
        end1=time()
        str(directMethod(L))
        end2=time()
        
        nedges.append(m)
        powiter.append(end1-start)
        directiter.append(end2-end1)
        totiter.append(end2-start)
        # print("Computing eigen vector through power iteration method" + "-> "+str(powerIteration(L,0.9)))
        # print("Computing the eigen vector through direct method"+"-> "+str(directMethod(L))+"\n")
    plt.plot(nedges,powiter)
    plt.plot(nedges,directiter)
    plt.plot(nedges,totiter)
    plt.xlabel("Number of Edges")
    plt.ylabel("Run time(in Secs)")
    plt.legend(["Power Iteration","Direct Method","Combined Runtime"])
    plt.show()
main()