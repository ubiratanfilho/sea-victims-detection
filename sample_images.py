# Dependencies
import torch
from torch import nn
from torchvision import transforms, datasets
from PIL import Image
import matplotlib.pyplot as plt

# Reading data
# images dir
train_dir = 'data/train'
test_dir = 'data/test'
# labels file
train_label_file = 'data/train.csv'

# load data
train_data = datasets.ImageFolder(train_dir[0:64], transform=transforms.ToTensor())

# define dataloaders
trainloader = torch.utils.data.DataLoader(train_data, batch_size=64, shuffle=True)

# plot images
images, labels = next(iter(trainloader))
fig, axes = plt.subplots(figsize=(10,4), ncols=4)
for ii in range(4):
    ax = axes[ii]
    ax.imshow(images[ii,0].numpy(), cmap='gray')
    ax.set_title(labels[ii])
plt.show()