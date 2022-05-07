import numpy as np
import numpy.linalg as la
np.set_printoptions(suppress=True)

def generateMatrix(edges,n,m):
    """This function generates a schotastic matrix from given edges between to nodes
        Arguments:-
            edges(list):- list of tuples (source,destination) where there is a directed edge from source to destination
            n(int):- number of nodes
            m(int):- number of directed edges
        Returns:-
            (numpy array) Schotastic matrix
    """
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        x,y = edges[i]
        c[y-1][x-1] = 1
    l = np.array(c)
    return (l+1e-10) / np.sum((l+1e-10), axis=0)

