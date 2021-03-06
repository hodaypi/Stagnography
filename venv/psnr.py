from math import log10, sqrt
import cv2
import numpy as np

def PSNR(before, after):
    mse = np.mean((before - after) ** 2)
    if(mse == 0): # MSE is zero means no noise is present in the signal .
        # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr

before = cv2.imread("before.png")
after = cv2.imread("after.png", 1)
value = PSNR(before, after)
print(f"PSNR value is {value} dB")

