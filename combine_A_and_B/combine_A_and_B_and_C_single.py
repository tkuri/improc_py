import os
import numpy as np
import cv2
import argparse
import glob

parser = argparse.ArgumentParser('create image pairs')
parser.add_argument('--file_A', dest='file_A', help='input image A', type=str, default='./img_A.png')
parser.add_argument('--file_B', dest='file_B', help='input image B', type=str, default='')
parser.add_argument('--file_C', dest='file_C', help='input image C', type=str, default='')
parser.add_argument('--file_ABC', dest='file_ABC', help='output image', type=str, default='./img_ABC.png')
args = parser.parse_args()

for arg in vars(args):
    print('[%s] = ' % arg, getattr(args, arg))

im_A = cv2.imread(args.file_A, 1) # python2: cv2.CV_LOAD_IMAGE_COLOR; python3: cv2.IMREAD_COLOR

if args.file_B=='':
    im_B = np.zeros(im_A.shape, dtype=np.uint8)
else:
    im_B = cv2.imread(args.file_B, 1) # python2: cv2.CV_LOAD_IMAGE_COLOR; python3: cv2.IMREAD_COLOR

if args.file_C=='':
    im_C = np.zeros(im_A.shape, dtype=np.uint8)
else:
    im_C = cv2.imread(args.file_C, 1) # python2: cv2.CV_LOAD_IMAGE_COLOR; python3: cv2.IMREAD_COLOR


im_ABC = np.concatenate([im_A, im_B, im_C], 1)
cv2.imwrite(args.file_ABC, im_ABC)
