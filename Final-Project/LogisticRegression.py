from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
import time
from torchvision import datasets, transforms
import torch

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

print("Fit the Logistic Regression model...")

timeList = []
trainList = []
testList = []

for i in range(100):
	print("NO. {} and max_iter is {}".format(i+1, i+1))
	start = time.time()
	clf = LogisticRegression(random_state=0, max_iter=i+1, solver='sag').fit(X_train, y_train)

	timespend = time.time() - start
	trainscore = clf.score(X_train, y_train)
	testscore = clf.score(X_test, y_test)

	print("\tTakes {:.4f}s to fit the Logistic Regression model!".format(timespend))
	print("\tTraining set score: " + str(trainscore))
	print("\tTesting set score: " + str(testscore))

	timeList.append(time.time() - start)
	trainList.append(trainscore)
	testscore.append(testscore)


import matplotlib.pyplot as plt

plt.rc('font', family='Times New Roman')
plt.style.use('ggplot')

fig, ax = plt.subplots()
ax.plot(range(1, len(timeList)+1), timeList)
ax.set_ylabel("Cumulated Variance Ration")
ax.set_xlabel("Number of Latent Variable(Components)")
# fig.savefig("Cumulated_Variance_Ration.png", dpi=300)
plt.show()

