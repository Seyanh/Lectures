import torch
import torchvision
import numpy as np
from sklearn.decomposition import PCA
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt


import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.optim.lr_scheduler import StepLR


class Net(nn.Module):
	def __init__(self):
		super(Net, self).__init__()
		self.alpha = 0.01

		self.main = nn.Sequential(
			# input is: batch_size x 1 x 28 x 28
			# 64 x 784 -> 64 x 512
			nn.Linear(128 * 128 * 3, 1024),
			nn.LeakyReLU(self.alpha, inplace=True),
			# 64 x 512 -> 64 x 256
			nn.Linear(1024, 1024),
			nn.LeakyReLU(self.alpha, inplace=True),
			nn.Linear(1024, 256),
			nn.LeakyReLU(self.alpha, inplace=True),
			nn.Linear(256, 64),
			nn.LeakyReLU(self.alpha, inplace=True),
			# 64 x 256 -> 64 x 1
			nn.Linear(64, 2),
		)

	def forward(self, x):
		x = self.main(x.view(-1, 128 * 128 * 3))
		output = F.log_softmax(x, dim=1)
		return output

def train(args, model, device, train_loader, optimizer, epoch):
	model.train()
	for batch_idx, (data, target) in enumerate(train_loader):
		data, target = data.to(device), target.to(device)
		optimizer.zero_grad()
		output = model(data)
		loss = F.nll_loss(output, target)
		loss.backward()
		optimizer.step()
		if batch_idx % 50 == 0:
			print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))



def test(model, device, test_loader):
	model.eval()
	test_loss = 0
	correct = 0
	with torch.no_grad():
		for data, target in test_loader:
			data, target = data.to(device), target.to(device)
			output = model(data)
			test_loss += F.nll_loss(output, target, reduction='sum').item()  # sum up batch loss
			pred = output.argmax(dim=1, keepdim=True)  # get the index of the max log-probability
			correct += pred.eq(target.view_as(pred)).sum().item()

	test_loss /= len(test_loader.dataset)

	print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))


def main():
	# Training settings、
	parser = argparse.ArgumentParser(description='PyTorch MNIST Example')
	parser.add_argument('--batch-size', type=int, default=64, help='input batch size for training (default: 64)')
	parser.add_argument('--test-batch-size', type=int, default=1000, metavar='N',
						help='input batch size for testing (default: 1000)')
	parser.add_argument('--epochs', type=int, default=25, metavar='N',
						help='number of epochs to train (default: 14)')
	parser.add_argument('--lr', type=float, default=0.001, metavar='LR', help='learning rate (default: 1.0)')
	parser.add_argument('--beta1', type=float, default=0.5, help='beta1 for adam. default=0.5')
	parser.add_argument("--beta2", type=float, default=0.999, help='beta2 for adam. default=0.999')
	parser.add_argument('--cuda', type=bool, default=True, help='enables CUDA training')
	args = parser.parse_args()

	args.cuda = args.cuda and torch.cuda.is_available()
	device = torch.device("cuda" if args.cuda else "cpu")

	transform = transforms.Compose([transforms.ToTensor()])

	train_dataset = datasets.ImageFolder(root='../data/train', transform=transform)
	train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True)

	test_dataset = datasets.ImageFolder(root='../data/test', transform=transform)
	test_loader = torch.utils.data.DataLoader(test_dataset, shuffle=True)

	model = Net().to(device)

	optimizer = torch.optim.Adam(model.parameters(), lr=args.lr, betas=(args.beta1, args.beta2))

	for epoch in range(1, args.epochs + 1):
		train(args, model, device, train_loader, optimizer, epoch)

if __name__ == '__main__':
	main()
