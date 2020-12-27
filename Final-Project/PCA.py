import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import time
from torchvision import datasets, transforms
import torch
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA

r"""
Loading Data ...
Loading Data ...
The data matrix shape is torch.Size([2000, 49152])
----------------------------------------
The result data matrix shape is (2000, 30)
----------------------------------------
Explained Variance:
[1396.80638764  307.58007045  188.74577827  160.47239533  106.04511682
   79.20163976   73.96882678   60.26002452   51.41304512   48.18908455
   43.07514344   36.85917409   33.38646715   29.12938954   26.46973213
   24.31362392   21.94020767   21.09314495   20.25993296   19.90083757
   18.05598986   17.15994724   16.78669993   16.18288479   15.31048359
   14.32524677   13.67856187   12.89718729   11.79102511   11.64391086]
Explained Variance Ration:
[0.36252008 0.07982778 0.04898613 0.0416482  0.02752241 0.02055559
 0.0191975  0.01563958 0.01334348 0.01250675 0.01117951 0.00956624
 0.00866496 0.00756009 0.00686982 0.00631024 0.00569425 0.00547441
 0.00525816 0.00516496 0.00468616 0.00445361 0.00435674 0.00420002
 0.00397361 0.0037179  0.00355006 0.00334727 0.00306018 0.003022  ]
Cumulated Variance Ration:
[0.3625200770564372, 0.44234785550022043, 0.491333981772941, 0.5329821769958336, 
0.5605045911703702, 0.5810601848454785, 0.6002576806620193, 0.6158972631591355, 
0.6292407452939974, 0.6417474969792459, 0.6529270022123285, 0.6624932461443266, 
0.6711582012520572, 0.6787182959328929, 0.6855881165586399, 0.6918983517452775, 
0.6975926024641009, 0.7030670108005044, 0.7083251715039561, 0.7134901344036753, 
0.7181762948421173, 0.7226299009032144, 0.7269866362422699, 0.7311866604491194, 
0.7351602660529307, 0.7388781682676941, 0.7424282331483539, 0.7457755040165855, 
0.7488356871380956, 0.7518576889707914]
Takes 110.30800294876099

Process finished with exit code 0
"""

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
pca = PCA(n_components=500)
pca.fit(X_train)

train_data_pca = pca.transform(X_train)
print("\tTakes {:.4f}s to fit the PCA model!".format(time.time() - start))
print("\t The result data matrix shape is " + str(train_data_pca.shape))

print("\n")

print("\t Explained Variance:")
print(pca.explained_variance_)
print("\t Explained Variance Ration:")
print(pca.explained_variance_ratio_)

cum_ratio = []
index = 0
for ratio in pca.explained_variance_ratio_:
	index += ratio
	cum_ratio.append(index)
print("\t Cumulated Variance Ration:")
print(cum_ratio)


import matplotlib.pyplot as plt

plt.rc('font', family='Times New Roman')
plt.style.use('ggplot')

fig, ax = plt.subplots()
ax.plot(range(1, len(cum_ratio)+1), cum_ratio)
ax.set_ylabel("Cumulated Variance Ration")
ax.set_xlabel("Number of Latent Variable(Components)")
fig.savefig("Cumulated_Variance_Ration.png", dpi=300)
plt.show()


fig, ax = plt.subplots()
ax.plot(range(1, 51), pca.explained_variance_ratio_[0:50])
ax.set_ylabel("Explained Variance Ration")
ax.set_xlabel("Number of Latent Variable(Components)")
fig.savefig("Explained_Variance_Ration.png", dpi=300)
plt.show()



"""
print("Fit the Logistic Regression model...")

start = time.time()
clf = LogisticRegression(random_state=0, max_iter=100).fit(train_data_pca, y_train)
print("Takes {:.4f}s to fit the Logistic Regression model!".format(time.time() - start))
print("Training set score: " + str(clf.score(train_data_pca, y_train)))

test_data_pca = pca.transform(X_test)
print("Testing set score: " + str(clf.score(train_data_pca, y_test)))
"""