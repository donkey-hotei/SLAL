from core.vector import Vector

"""
The Gram-Smidt process of
orthogonalization. Which uses projection to 
find a set a of orthogonal vectors. 
"""

def project_along(b, v, eps = 1E-20):
    '''
    Project b along v.

    Input:
        - b: a Vector
        - v: a Vector
        - eps (default: 1E-20): threshold below which squared norms are considered zero

    Output:
        - a Vector representing the projection of b onto v
    '''
    sigma = ((b*v)/(v*v)) if v*v > eps else 0
    return sigma * v

def project_orthogonal(b, vlist):
    '''
    Project b orthogonal to vlist.

    Input:
        - b: a Vector 
        - vlist: a list of Vectors

    Output: the projection of b orthogonal to the Vectors in vlist
    '''
    for v in vlist:
        b = b - project_along(b, v)
    return b

def aug_project_orthogonal(b, vlist, eps = 1E-20):
    alphadict = {len(vlist):1}
    for i,v in enumerate(vlist):
        sigma = (b*v)/(v*v) if v*v > eps else 0
        alphadict[i] = sigma
        b = b - sigma*v
    return (b, alphadict)

def orthogonalize(vlist):
    '''
    Orthogonalizes vlist preserving order.
    The ith vector in the output list is the projection of vlist[i] orthogonal to
    the space spanned by all the previous vectors in the output list.

    Input: a list of Vectors

    Output: a list of mutually orthogonal Vecs spanning the same space as the input Vecs
    '''
    assert isinstance(vlist, list)
    vstarlist = []
    for v in vlist:
        vstarlist.append(project_orthogonal(v, vstarlist))
    return vstarlist

def aug_orthogonalize(vlist):
    '''
    Input: a list of Vectors
    Output: a list of orthonormal Vectors spanning the same space as the input Vecs
    '''
    assert isinstance(vlist, list)
    vstarlist = []
    sigma_vecs = []
    D = set(range(len(vlist)))
    for v in vlist:
        (vstar, sigmadict) = aug_project_orthogonal(v, vstarlist)
        vstarlist.append(vstar)
        sigma_vecs.append(Vec(D, sigmadict))
    return vstarlist, sigma_vecs
