# Data class for reading and preparing data


import torch
from torchvision import datasets, models, transforms
import os



class DataRead(object):
    def __init__(self):
        pass

    def read_data(self):
        data_transforms = {'train': transforms.Compose([transforms.RandomResizedCrop(32),
                                                        transforms.RandomHorizontalFlip(),
                                                        transforms.ToTensor(),
                                                        transforms.Normalize([0.485, 0.456, 0.406],
                                                                             [0.229, 0.224, 0.225])]),
                           'val': transforms.Compose([transforms.Resize(256),
                                                      transforms.CenterCrop(32),
                                                      transforms.ToTensor(),
                                                      transforms.Normalize([0.485, 0.456, 0.406],
                                                                           [0.229, 0.224, 0.225])])}


        data_dir = 'E:/chestXray'
        image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x), data_transforms[x]) for x in
                          ['train', 'val']}
        dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=4, shuffle=True) for x in
                       ['train', 'val']}
        dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'val']}
        class_names = image_datasets['train'].classes

        return dataloaders, class_names,dataset_sizes
