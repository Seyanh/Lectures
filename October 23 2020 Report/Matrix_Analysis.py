import numpy as np

matrix = np.mat([[8, 1, 6], [3, 5, 7], [4, 9, 2]])
print("\n")

# 通过实对称矩阵进行验证
matrix = np.mat([[8, 3, 6], [3, 5, 9], [6, 9, 2]])
print("研究对象是实对称矩阵: \n " + str(matrix) + "\n")

print("\n" + "-" * 50 + "\n")

Evals, Evecs = np.linalg.eig(matrix)
print("特征值是: \n" + str(Evals) + "\n")
print("特征向量是: \n" + str(Evecs) + "\n")
Evals = np.mat(np.diag(Evals))
reconstruct = Evecs * Evals * Evecs.T

# 得出结论矩阵的特征向量是V * D * V^T
print("特征值重构回矩阵结果: \n" + str(reconstruct))

# 分界线
print("\n" + "-" * 50 + "\n")

u, s, vh = np.linalg.svd(matrix, full_matrices=True)

# 注意到SVD分解的特征值是排列了大小顺序的
print("奇异值是: \n" + str(s) + "\n")
print("左奇异矩阵: \n" + str(u) + "\n")
# 显示还是应该原本右奇异矩阵,则应该转置一下
print("右奇异矩阵: \n" + str(vh.T) + "\n") 
s = np.mat(np.diag(s))
reconstruct = u * s * vh

# 得出结论矩阵的奇异值分解是 U * D * V (V已经是转置过后的矩阵)
print("奇异值重构回矩阵结果: \n" + str(reconstruct))

# A^T*A得到的特征向量是U
print("\n" + "-" * 50 + "\n")

ATAmatrix = matrix.T * matrix
Evals, Evecs = np.linalg.eig(ATAmatrix)
print("A^T*A是: \n" + str(ATAmatrix) + "\n")
print("A^T*A的特征值是: \n" + str(Evals) + "\n")
print("A^T*A的特征值根号是: \n" + str(np.sqrt(Evals)) + "\n")
print("A^T*A的特征向量是: \n" + str(Evecs) + "\n")

V = Evecs

# A*A^T得到的特征向量是V
print("\n" + "-" * 50 + "\n")

AATmatrix = matrix * matrix.T
Evals, Evecs = np.linalg.eig(AATmatrix)
print("A*A^T是: \n" + str(AATmatrix) + "\n")
print("A*A^T的特征值是: \n" + str(Evals) + "\n")
print("A*A^T的特征值根号是: \n" + str(np.sqrt(Evals)) + "\n")
print("A*A^T的特征向量是: \n" + str(Evecs) + "\n")

U = Evecs