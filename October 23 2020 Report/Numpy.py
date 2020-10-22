import numpy as np

# Vector Generation
vec = np.array([1,2,3,4])
print(vec)
print(np.shape(vec))
print(vec.shape)
print('Broadcasting: ', vec + 1)
print('Sum: ', vec.mean())
print('Vectorization: ', vec**2, vec + vec)

## Matrix Generation
myZero = np.zeros([3,5]) # generate a 3*5 zero matrix
print(myZero)
myOnes = np.ones([3,5]) # generate a 3*5 ones matrix
print(myOnes)
myRand = np.random.rand(3,5) # generate a 3*5 matrix with the number in (0~1)
print(myRand)
myEyes = np.eye(3,5) # generate a 3*5 identity matrix, np.eye(3) will get a square matrix
print(myEyes)
print('Matrix Stack: Horizontal\n', np.hstack((myZero, myOnes)))
print('Matrix Stack: Verticle\n', np.vstack((myZero, myOnes)))

# Matrix Operations
myOnes = np.ones([3, 5])
myEyes = np.eye(3, 5)
print('myOnes:\n', myOnes)
print('myEyes:\n', myEyes)
# Visit elements:
print(myEyes[1, 1], myEyes[1][1])
# Matrix Sum
print('Sum of Matrix:myOnes+myEyes\n', myOnes + myEyes)
# sum of all elements of Matrix
print('Sum of elements: np.sum(myOnes)\n', np.sum(myOnes))
print('Sum of each columns: sum(myOnes)\n', sum(myOnes))
# Matrix Multiplication
NewMat = np.mat([[1, 2, 3], [2, 3, 1], [1, 0, 0]])
print('Matrix:\n', NewMat)
print('Scalar Matrix Multiplication:\n', 10*NewMat)
print('Matrix Multiplication:\n', NewMat*NewMat)
print('Matrix Elements Multiplication: np.multiply\n', np.multiply(NewMat, NewMat))
print('Matrix Elements Power: np.power\n', np.power(NewMat, 2))


## Matrix Transpose
NewMat = np.mat([[1,2,3],[4,5,6],[7,8,9]])
print('Matrix: \n',NewMat)
print('Matrix Transpose:\n',NewMat.T)
print('Matrix after .T: \n', NewMat)
print('Matrix Transpose:\n', NewMat.transpose()) ## same as the .T
print('Matrix after Transpose():\n', NewMat)



## Matrix Shape, Copy, slice, split...

NewMat = np.mat([[1,2,3],[4, 5, 6],[7, 8, 9 ],[10,1,1]])
[m,n] = np.shape(NewMat)
print('Matrix:\n',NewMat)
print('Row and Columns:', m,n)
print('First Row:', NewMat[0]) # same as: NewMat[0,](Bad) and NewMat[0,:]
print('First Column:', NewMat.T[0])
print('Matrix Elements: ', NewMat[2,1]) ## Notice: first number is 0!!!!
print('Matrix Rows:\n', NewMat[[0,1],:]) ## first two rows
print('Matrix Colmuns:\n', NewMat[:,[1,2]])
# copy a matrix to other variable
NewMat2 = NewMat.copy()
# compare two matrix by elements
print(NewMat<NewMat2)
print('New Shape: \n', NewMat.reshape((2,6)))


## Linear Algebra
NewMat = np.mat([[1,2,3],[4,5,6],[1,0,0]])
print("matrix:\n",NewMat)
print('Determinant:', np.linalg.det(NewMat))
print('Inverse Matrix:\n', np.linalg.inv(NewMat))
print('check: inv(A)*A\n', np.linalg.inv(NewMat)*NewMat)
print('Rank:\n', np.linalg.matrix_rank(NewMat))
b = [1,2,1]
print('Solve Linear System:\n', np.linalg.solve(NewMat, b))
b2 = [1,2,1]
b2T = np.mat(b2).T
print('Check by: inv(A)*b\n', np.linalg.inv(NewMat)*b2T)
# Eigen values
Evals, Evecs = np.linalg.eig(NewMat)
print('Eigen values: \n', Evals)
print('Eigen Vectors:\n', Evecs) #NOTICE: eigenvectors are stored in columns
print('AX , lambda*X:\n', NewMat*Evecs[:,0], Evals[0]*Evecs[:,0])
# use similarity matrix
sigma = Evals * np.eye(3)
print('sigma,\n ',sigma)
print('V*sigma*V^-1 = A:\n', Evecs*sigma*np.linalg.inv(Evecs))


import numpy as np
import matplotlib.pyplot as plt
file = './Data/digits.csv'
digits = np.loadtxt(file, delimiter=',')
print(type(digits))
# Select and reshape a row
im = digits[25, 1:]
im_sq = np.reshape(im, (28, 28))
# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()






