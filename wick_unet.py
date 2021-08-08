import torch
import torch.nn as nn


class Encoder(nn.Module):
    def __init__(self, channels=[3, 40, 60, 120, 160, 240], kernel=5, padding=2, pool_kernel=2):
        super().__init__()
        self.conv1 = nn.Conv2d(channels[0], channels[1], kernel, padding=padding)
        self.conv2 = nn.Conv2d(channels[1], channels[2], kernel, padding=padding)
        self.conv3 = nn.Conv2d(channels[2], channels[3], kernel, padding=padding)
        self.conv4 = nn.Conv2d(channels[3], channels[4], kernel, padding=padding)
        self.conv5 = nn.Conv2d(channels[4], channels[5], kernel, padding=padding)
        
        self.relu = nn.ReLU()
        # setting stride to equal kernel
        self.pool = nn.MaxPool2d(pool_kernel, stride=pool_kernel)
    
    def forward(self, x):
        x = self.conv2(self.relu(self.conv1(x)))
        x = self.pool(x)
        x = self.conv4(self.relu(self.conv3(x)))
        x = self.pool(x)
        
        return self.relu(self.conv5(x))


class Decoder(nn.Module):
    def __init__(self, channels=[240, 120, 60, 2, 1], kernel=5, padding=2, mid_kernel=2):
        super().__init__()
        self.deconv1 = nn.ConvTranspose2d(channels[0], channels[1], kernel, padding=padding)
        # kernel and stride to match the pool layer in the encoder
        self.deconv2 = nn.ConvTranspose2d(channels[1], channels[2], mid_kernel, stride=mid_kernel)
        self.deconv3 = nn.ConvTranspose2d(channels[2], channels[3], mid_kernel, stride=mid_kernel)
        # for generating output (out channel is 1 mask is one layer)
        self.deconv4 = nn.ConvTranspose2d(channels[3], channels[4], kernel, padding=padding)
    
        self.relu = nn.ReLU()
        
    def forward(self, x):
        x = self.relu(self.deconv1(x))
        x = self.relu(self.deconv2(x))
        return self.deconv4(self.deconv3(x))


class WickUnet(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = Encoder()
        self.decoder = Decoder()

    def forward(self, x):
        return self.decoder(self.encoder(x))