import torch
import torchvision
from torch import nn
class ZH_MNIST(nn.Module):
    def __init__(self):
        super(ZH_MNIST, self).__init__()
        # 假设batch_size = 64
        self.module = nn.Sequential(
            # input: 64x3x64x64
            nn.Conv2d(in_channels=3, out_channels=8, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            # size: 64x8x32x32
            nn.Conv2d(in_channels=8, out_channels=16, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            # size: 64x16x16x16
            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            # size: 64x32x8x8
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            # size: 64x64x8x8
            nn.Flatten(),
            # FC1
            nn.Linear(in_features=64*8*8, out_features=128),
            nn.ReLU(),
            # 正则化
            nn.Dropout(p=0.4),
            # FC2
            nn.Linear(in_features=128, out_features=10),
            nn.Softmax(dim=1)
        )
    def forward(self, input):
        output = self.module(input)
        return output