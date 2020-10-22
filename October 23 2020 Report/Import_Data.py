FileName = './Data/cars.txt'
fid = open(FileName, 'r')
print(fid.read())
fid.close()


with open(FileName, 'r') as fid:
    print(fid.readline())
    print(fid.readline())


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
