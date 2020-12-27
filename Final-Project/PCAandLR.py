import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import time
from torchvision import datasets, transforms
import torch
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA

print("Start to load the data!")

transform = transforms.Compose([transforms.ToTensor()])

print("\t Loading training data ...")
train_dataset = datasets.ImageFolder(root='../data/train/', transform=transform)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=4000, drop_last=True, shuffle=True)

print("\t Loading testing data ...")
test_dataset = datasets.ImageFolder(root='../data/test/', transform=transform)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=1200, drop_last=True, shuffle=False)

global data, target
for batch_idx, (data, target) in enumerate(train_loader):
	data = data
	target = target

global test_data, test_target
for batch_idx, (test_data, test_target) in enumerate(test_loader):
	test_data = test_data
	test_target = test_target

print("\n")
X_train = data.view(-1, 128 * 128 * 3)
y_train = target.view(-1)
X_test = test_data.view(-1, 128 * 128 * 3)
y_test = test_target.view(-1)

X_train = preprocessing.scale(X_train)
X_test = preprocessing.scale(X_test)
print("The data matrix shape is " + str(X_train.shape))
print("The target matrix shape is " + str(y_train.shape))
print("The test data matrix shape is " + str(X_test.shape))
print("The test target matrix shape is " + str(y_test.shape))

print("\n")

print("Fit the PCA model...")
start = time.time()
pca = PCA(n_components=100)
pca.fit(X_train)
train_data_pca = pca.transform(X_train)

print("The data matrix shape is " + str(train_data_pca.shape))
print("The target matrix shape is " + str(y_train.shape))
print("\n")

print("Fit the Logistic Regression model...")
start = time.time()
clf = LogisticRegression(random_state=0, max_iter=100, solver='sag').fit(train_data_pca, y_train)
print("Takes {:.4f}s to fit the Logistic Regression model!".format(time.time() - start))
print("Training set score: " + str(clf.score(train_data_pca, y_train)))

test_data_pca = pca.transform(X_test)
print("Testing set score: " + str(clf.score(test_data_pca, y_test)))
