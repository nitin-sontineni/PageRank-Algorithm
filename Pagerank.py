import numpy as np
import numpy.linalg as la
np.set_printoptions(suppress=True)


def powerIteration(probabilityMatrix,d):
    """This function provides the PageRank for the websites in the internet by solving the eigen vector using power iteration

        Arguments:- 
                (probabilityMatrix(numpy 2D array): A probability matrix for the websites
                    d(float): damping factor
        Returns:-
                    ranking matrix(numpy array): Array with the PageRank of websites
    """
    n = probabilityMatrix.shape[0]
    M = d*probabilityMatrix + (1-d)/n * np.ones([n,n])
    r = 100 * np.ones(n) / n
    last = r
    r = M @ r
    while la.norm(last - r) > 0.01 :
        last = r
        r = M @ r
    return r

def directMethod(probabilityMatrix):
    """
        This function provides the PageRank of the websites in the internet by solving the eign vector using packages from python

        Arguments:- 
                (probabilityMatrix(numpy 2D array): A probability matrix for the websites
        Returns:-
                    numpy array with PageRanks of the websites

    """
    #This function doesn't take damping input so it may give different results than that of powerIteration function
    eVals, eVecs = la.eig(probabilityMatrix) 
    # Gets the eigenvalues and vectors of the probability matrix
    order = np.absolute(eVals).argsort()[::-1] 
    # Orders them by their eigenvalues
    eVals = eVals[order]
    eVecs = eVecs[:,order]

    r = eVecs[:, 0]
    return 100 * np.real(r / np.sum(r))