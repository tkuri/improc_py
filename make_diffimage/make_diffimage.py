import numpy as np
import cv2
import sys
import os
from skimage.measure import compare_ssim, compare_psnr

def diffimg(gt, comp, out, gain=4.0):
    print(gt, comp)
    img1 = cv2.imread(gt)
    img2 = cv2.imread(comp)
    diff = abs(np.float64(img1) - np.float64(img2))
    cv2.imwrite(out, diff*gain)
    print(compare_ssim(img1, img2, multichannel=True))
    print(compare_psnr(img1, img2))

if __name__ == '__main__':
    args = sys.argv

    dir = args[1]
    gt = dir+'gt.png'
    # complist = ['cooktorrance.png', 'walter.png', 'brady.png', 'nas_seed230.png']
    complist = ['blinnphong.png', 'cooktorrance.png', 'walter.png', 'brady.png', 'nas_seed230.png']
    for c in complist:
        out = dir+os.path.splitext(os.path.basename(c))[0]
        out += '_diff.png'
        diffimg(gt, dir+c, out)