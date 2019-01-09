# Author : @ Kishore Malik

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import torchvision
from torch.autograd import Variable
from torchvision import datasets, models, transforms
import os
import numpy as np
import Training as tr

from Data import DataRead
import Model as md
from utilData import parser

data = DataRead()
dataloaders, class_names, dataset_sizes =data.read_data()

args=parser()

block_config = [(100 - 4) // 6 for _ in range(3)]


model = md.DenseNet(
        growth_rate=12,
        block_config=block_config,
        num_classes=2,
        small_inputs=True,
        efficient=True,
    )
if torch.cuda.is_available():
    model=model.cuda()

criterian=nn.CrossEntropyLoss()
optimizer=optim.SGD(model.parameters(),lr=0.001,momentum=0.9)
exp_lr_scheduler=lr_scheduler.StepLR(optimizer, step_size=7, gamma=0.1)
#print(exp_lr_scheduler)

print(model)

tr.train(dataloaders, model, criterian, optimizer, dataset_sizes,exp_lr_scheduler)

