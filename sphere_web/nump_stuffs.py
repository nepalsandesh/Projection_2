# # np.linalg is a module in the NumPy library that provides functions for linear algebra operations. 
# The functions in np.linalg are implemented using highly optimized C and Fortran libraries and are designed 
# to handle large arrays and matrices efficiently.

# Some of the common functions in np.linalg include:

# np.linalg.inv: Computes the (multiplicative) inverse of a matrix.
# np.linalg.det: Computes the determinant of a matrix.
# np.linalg.eig: Computes the eigenvalues and eigenvectors of a square matrix.
# np.linalg.svd: Computes the singular value decomposition of a matrix.
# np.linalg.solve: Solves a linear system of equations using matrix decomposition.
# np.linalg.norm: Computes various matrix and vector norms values.


# Here's an example to illustrate the use of np.linalg.norm:


import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.linalg.norm(a)
d = np.linalg.norm(b)
e = np.linalg.norm(a - b)

# print(c)
# print(d)
# print(e)




# np.vstack() is a function in the NumPy library that is used to stack arrays vertically,
# i.e. to join a sequence of arrays along the first (vertical) axis. The function takes a sequence of 
# arrays as input and returns a single array with the arrays stacked on top of each other.

# Here's an example to illustrate the use of np.vstack():

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.vstack((a, b))
# print(c)




# np.meshgrid

aa = np.array([1,2,3])
bb = np.array([4,5,6,7])

mm = np.meshgrid(aa,bb)

print(mm[1])