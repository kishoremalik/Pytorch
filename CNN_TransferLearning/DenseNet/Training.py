from utilData import parser
import torch
from torch.autograd import Variable

args1=parser()


def train(dataloaders, model, criterian, optimizer, dataset_sizes,exp_lr_scheduler):
    """Train for one epoch on the training set"""

    num_epochs = 25
    for epoch in range(num_epochs):
        exp_lr_scheduler.step()


        # Reset the correct=0 after passing through all the dataset
        correct = 0
        for images, labels in dataloaders['train']:
            images = Variable(images)
            labels = Variable(labels)
            if torch.cuda.is_available():
                images = images.cuda()
                labels = labels.cuda()
            optimizer.zero_grad()
            output = model(images)
            loss = criterian(output, labels)
            loss.backward()
            optimizer.step()
            _, predicted = torch.max(output, 1)
            correct += (predicted == labels).sum()
        train_acc = 100 * correct / dataset_sizes['train']
        print('training start')
        print('Epoch [{}/{}] , loss: {:.4f}, Train Accuracy {} %'.format(epoch + 1, num_epochs, loss.item(), train_acc))

    torch.save(model.state_dict(), 'E:\model_save\DenseNet_chestXray\dnchestModel.pth.tar')




