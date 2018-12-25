# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


img1 = io.imread('img/pic1.jpg')
img1=img1.resize((500,400),Image.BICUBIC)
plt.figure(figsize=(10,10)), plt.imshow(img1)