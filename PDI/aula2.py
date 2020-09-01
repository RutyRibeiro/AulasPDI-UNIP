import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread("kk.png",0)
plt.hist(img.ravel(),256,[0,256])
plt.show()
