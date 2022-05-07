
from Pagerank import powerIteration
from Pagerank import directMethod
from stochasticMatrix import generateMatrix


def main():
    """Driver code for calculating the required principle left eigen vectors
    """
    names_website = []
    edges = []
    print('Enter number of website links in the sample internet :-')
    n = int(input())
    if n == 0:
        print("Number of nodes should be greater than equal to one \n")
        return 
    print('\n')
    print('Enter the names of the website links :-')
    for _ in range(n):
        names_website.append(input())
    print('\n')
    for i in range(n):
        print(str(i+1) + '->'+names_website[i])
    print('\n')
    print('Enter total number of edges in the directed graph:- ')
    m = int(input())
    print('The edges are:- ')
    for _ in range(m):
        edges.append(tuple(map(int,input().split(","))))
    L = generateMatrix(edges,n,m)
    print('\n')

    print("Computing eigen vector through power iteration method" + "-> "+str(powerIteration(L,0.9)))
    print("Computing the eigen vector through direct method"+"-> "+str(directMethod(L))+"\n")

main()



