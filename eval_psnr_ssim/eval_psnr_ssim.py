import numpy as np
import cv2
import argparse
import skimage
skimage_version = float(skimage.__version__[2:])
if skimage_version >= 16.0:
    from skimage.metrics import structural_similarity
    from skimage.metrics import peak_signal_noise_ratio
else:
    from skimage.measure import compare_ssim as structural_similarity
    from skimage.measure import compare_psnr as peak_signal_noise_ratio

MAX_8BIT = 255.
MAX_16BIT = 65535.

def parser():
    parser = argparse.ArgumentParser(description='Evaluate PRNR and SSIM')
    parser.add_argument('-r', '--ref', default='', type=str, help='Reference image')
    parser.add_argument('-i', '--input', default='', type=str, help='Input image')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parser()
    ref = cv2.imread(args.ref)
    img = cv2.imread(args.input)
    print(structural_similarity(ref, img, data_range=int(MAX_8BIT), multichannel=True))
    print(peak_signal_noise_ratio(ref, img, data_range=int(MAX_8BIT)))
 