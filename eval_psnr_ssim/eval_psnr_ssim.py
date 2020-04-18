import numpy as np
import cv2
from skimage.measure import compare_ssim, compare_psnr

if __name__ == '__main__':
    img1 = cv2.imread("gt.png")
    img2 = cv2.imread("blinnphong.png")
    print(compare_ssim(img1, img2, multichannel=True))
    print(compare_psnr(img1, img2))
 