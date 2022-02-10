import numpy as np
import matplotlib.pyplot as plt
import cv2
import argparse
import bm3d
import os
import csv

def parser():
    parser = argparse.ArgumentParser(description='Apply BM3D to image')
    parser.add_argument('file_name', help='Trager Image file')
    parser.add_argument('--x', type=int, default=13, help='Left Top of the Region')
    parser.add_argument('--y', type=int, default=5, help='Left Top of the Region')
    parser.add_argument('--w', type=int, default=200, help='Width of the Region')
    parser.add_argument('--h', type=int, default=185, help='height of the Region')
    # parser.add_argument('--step_w', type=int, default=23, help='Step of width arrows')
    # parser.add_argument('--step_h', type=int, default=30, help='Step of height arrows')
    parser.add_argument('--step_w', type=int, default=16, help='Step of width arrows')
    parser.add_argument('--step_h', type=int, default=20, help='Step of height arrows')
    parser.add_argument('--power', type=float, default=80.0, help='Power of arrows')
    args = parser.parse_args()
    return args

def main():
    args = parser()
    fname = args.file_name
    arrows_name = os.path.split(fname)[0] + '/' + os.path.splitext(os.path.basename(fname))[0] + '_arrows.png'

    img = cv2.imread(fname)
    org_size = img.shape
    scl = 5.0

    img = cv2.resize(img , (int(org_size[1]*scl), int(org_size[0]*scl)))    
    img_f = img.astype(float) / 255.0
    cnt = 0.5
    width = img.shape[1]
    height = img.shape[0]
    ambiInv = False
    power = args.power * scl

    for y in range(int(args.y*scl), int((args.y+args.h)*scl), int(args.step_h*scl)):
        for x in range(int(args.x*scl), int((args.x+args.w)*scl), int(args.step_w*scl)):
            v = img_f[y, x]

            v[1] = cnt - v[1]
            v[2] = v[2] - cnt

            if ambiInv:
                v[1] = -v[1]
                v[2] = -v[2]

            ex = x + v[2] * power
            ey = y + v[1] * power

            ex = min(max(0, int(ex)), width - 1)
            ey = min(max(0, int(ey)), height - 1)

            sp = (x, y)
            ep = (ex, ey)

            clr = img[y, x]
            # img = cv2.arrowedLine(img, sp, ep, (0, 75, 255), thickness=7,  tipLength=0.2) # Red
            # img = cv2.arrowedLine(img, sp, ep, (130, 128, 255), thickness=7,  tipLength=0.2) # Pink
            img = cv2.arrowedLine(img, sp, ep, (128, 255, 255), thickness=7,  tipLength=0.2) # Cream
            # img = cv2.arrowedLine(img, sp, ep, (int(clr[1]), int(clr[2]), int(clr[0])), thickness=7,  tipLength=0.2)

    cv2.imwrite(arrows_name, img)



if __name__ == "__main__":
    main()    