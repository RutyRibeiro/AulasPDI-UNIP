import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread("kk.png")
color=('r','g','b')

for i,col in enumerate(color):
    his=cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(his,color=col)
    plt.xlim([0,256])
plt.show()