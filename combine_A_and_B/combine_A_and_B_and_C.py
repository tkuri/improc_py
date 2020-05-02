import os
import numpy as np
import cv2
import argparse
import glob

parser = argparse.ArgumentParser('create image pairs')
parser.add_argument('--fold_A', dest='fold_A', help='input directory for image A', type=str, default='./data/train_data/top_pred')
parser.add_argument('--fold_B', dest='fold_B', help='input directory for image B', type=str, default='./data/train_data/top_gt')
parser.add_argument('--fold_C', dest='fold_C', help='input directory for image C', type=str, default='./data/train_data/light_pred')
parser.add_argument('--fold_ABC', dest='fold_ABC', help='output directory', type=str, default='./data/train_data/out')
parser.add_argument('--name_ABC', dest='name_ABC', help='output file name', type=str, default='cmb')
parser.add_argument('--num_imgs', dest='num_imgs', help='number of images', type=int, default=1000000)
args = parser.parse_args()

for arg in vars(args):
    print('[%s] = ' % arg, getattr(args, arg))

splits = os.listdir(args.fold_A)

for sp in splits:
    img_fold_A = os.path.join(args.fold_A, sp)
    img_fold_B = os.path.join(args.fold_B, sp)
    img_fold_C = os.path.join(args.fold_C, sp)
    img_list_A = sorted(glob.glob(img_fold_A+'/*.png'))
    img_list_A = [os.path.basename(file) for file in img_list_A]
    img_list_B = sorted(glob.glob(img_fold_B+'/*.png'))
    img_list_B = [os.path.basename(file) for file in img_list_B]
    img_list_C = sorted(glob.glob(img_fold_C+'/*.png'))
    img_list_C = [os.path.basename(file) for file in img_list_C]
    # img_list_A = os.listdir(img_fold_A)
    # img_list_B = os.listdir(img_fold_B)
    # img_list_C = os.listdir(img_fold_C)

    num_imgs = min(args.num_imgs, len(img_list_A))
    print('split = %s, use %d/%d images' % (sp, num_imgs, len(img_list_A)))
    img_fold_ABC = os.path.join(args.fold_ABC, sp)
    if not os.path.isdir(img_fold_ABC):
        os.makedirs(img_fold_ABC)
    print('split = %s, number of images = %d' % (sp, num_imgs))
    for n in range(num_imgs):
        name_A = img_list_A[n]
        path_A = os.path.join(img_fold_A, name_A)
        name_B = img_list_B[n]
        path_B = os.path.join(img_fold_B, name_B)
        name_C = img_list_C[n]
        path_C = os.path.join(img_fold_C, name_C)
        if os.path.isfile(path_A) and os.path.isfile(path_B) and os.path.isfile(path_C):
            print('A:{}, B:{}, C:{}'.format(path_A, path_B, path_C))
            name_ABC = '{}_{}.png'.format(args.name_ABC, str(n).zfill(4))
            path_ABC = os.path.join(img_fold_ABC, name_ABC)
            im_A = cv2.imread(path_A, 1) # python2: cv2.CV_LOAD_IMAGE_COLOR; python3: cv2.IMREAD_COLOR
            im_B = cv2.imread(path_B, 1) # python2: cv2.CV_LOAD_IMAGE_COLOR; python3: cv2.IMREAD_COLOR
            im_C = cv2.imread(path_C, 1) # python2: cv2.CV_LOAD_IMAGE_COLOR; python3: cv2.IMREAD_COLOR
            im_ABC = np.concatenate([im_A, im_B, im_C], 1)
            cv2.imwrite(path_ABC, im_ABC)
