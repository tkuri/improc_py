import os
import cv2
import argparse

def parser():
    parser = argparse.ArgumentParser(description='Convert colormap')
    parser.add_argument('img_name', help='Input file name')
    args = parser.parse_args()
    return args

def main():
    args = parser()
    im = cv2.imread(args.img_name,  cv2.IMREAD_GRAYSCALE)
    imC = cv2.applyColorMap(im, cv2.COLORMAP_HOT)
    out_name = os.path.splitext(os.path.basename(args.img_name))[0] + '_colormap.png'
    cv2.imwrite(out_name, imC)

if __name__ == "__main__":
    main()