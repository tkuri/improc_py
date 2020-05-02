import os
import numpy as np
import cv2
import argparse
import glob

parser = argparse.ArgumentParser('create image pairs')
parser.add_argument('--fold_A', dest='fold_A', help='input directory for image A', type=str, default='./data/train_data/input')
parser.add_argument('--fold_B', dest='fold_B', help='input directory for image B', type=str, default='./data/train_data/top_gt')
parser.add_argument('--fold_C', dest='fold_C', help='input directory for image C', type=str, default='./data/train_data/light_pred')
parser.add_argument('--fold_D', dest='fold_D', help='input directory for image D', type=str, default='./data/train_data/top_pred')
parser.add_argument('--fold_ABCD', dest='fold_ABCD', help='output directory', type=str, default='./data/train_data/out')
parser.add_argument('--name_ABCD', dest='name_ABCD', help='output file name', type=str, default='cmb')
parser.add_argument('--num_imgs', dest='num_imgs', help='number of images', type=int, default=1000000)
args = parser.parse_args()

for arg in vars(args):
    print('[%s] = ' % arg, getattr(args, arg))

splits = os.listdir(args.fold_A)

for sp in splits:
    img_fold_A = os.path.join(args.fold_A, sp)
    img_fold_B = os.path.join(args.fold_B, sp)
    img_fold_C = os.path.join(args.fold_C, sp)
    img_fold_D = os.path.join(args.fold_D, sp)
    img_list_A = sorted(glob.glob(img_fold_A+'/*.png'))
    img_list_A = [os.path.basename(file) for file in img_list_A]
    img_list_B = sorted(glob.glob(img_fold_B+'/*.png'))
    img_list_B = [os.path.basename(file) for file in img_list_B]
    img_list_C = sorted(glob.glob(img_fold_C+'/*.png'))
    img_list_C = [os.path.basename(file) for file in img_list_C]
    img_list_D = sorted(glob.glob(img_fold_D+'/*.png'))
    img_list_D = [os.path.basename(file) for file in img_list_D]
    # img_list_A = os.listdir(img_fold_A)
    # img_list_B = os.listdir(img_fold_B)
    # img_list_C = os.listdir(img_fold_C)
    # img_list_D = os.listdir(img_fold_D)

    num_imgs = min(args.num_imgs, len(img_list_A))
    print('split = %s, use %d/%d images' % (sp, num_imgs, len(img_list_A)))
    img_fold_ABCD = os.path.join(args.fold_ABCD, sp)
    if not os.path.isdir(img_fold_ABCD):
        os.makedirs(img_fold_ABCD)
    print('split = %s, number of images = %d' % (sp, num_imgs))
    for n in range(num_imgs):
        name_A = img_list_A[n]
        path_A = os.path.join(img_fold_A, name_A)
        name_B = img_list_B[n]
        path_B = os.path.join(img_fold_B, name_B)
        name_C = img_list_C[n]
        path_C = os.path.join(img_fold_C, name_C)
        name_D = img_list_D[n]
        path_D = os.path.join(img_fold_D, name_D)
        if os.path.isfile(path_A) and os.path.isfile(path_B) and os.path.isfile(path_C) and os.path.isfile(path_D):
            print('A:{}, B:{}, C:{}, D:{}'.format(path_A, path_B, path_C, path_D))
            name_ABCD = '{}_{}.png'.format(args.name_ABCD, str(n).zfill(4))
            path_ABCD = os.path.join(img_fold_ABCD, name_ABCD)
            im_A = cv2.imread(path_A, 1) # python2: cv2.CV_LOAD_IMAGE_COLOR; python3: cv2.IMREAD_COLOR
            im_B = cv2.imread(path_B, 1) # python2: cv2.CV_LOAD_IMAGE_COLOR; python3: cv2.IMREAD_COLOR
            im_C = cv2.imread(path_C, 1) # python2: cv2.CV_LOAD_IMAGE_COLOR; python3: cv2.IMREAD_COLOR
            im_D = cv2.imread(path_D, 1) # python2: cv2.CV_LOAD_IMAGE_COLOR; python3: cv2.IMREAD_COLOR
            im_ABCD = np.concatenate([im_A, im_B, im_C, im_D], 1)
            cv2.imwrite(path_ABCD, im_ABCD)
