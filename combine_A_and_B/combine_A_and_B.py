import os
import numpy as np
import cv2
import argparse

parser = argparse.ArgumentParser('create image pairs')
parser.add_argument('--fold_A', dest='fold_A', help='input directory for image A', type=str, default='./data/train_data/top_pred')
parser.add_argument('--fold_B', dest='fold_B', help='input directory for image B', type=str, default='./data/train_data/top_gt')
parser.add_argument('--fold_AB', dest='fold_AB', help='output directory', type=str, default='./data/train_data/cbox_top_pred_to_gt')
parser.add_argument('--name_AB', dest='name_AB', help='output file name', type=str, default='top_pred_and_top_gt')
parser.add_argument('--num_imgs', dest='num_imgs', help='number of images', type=int, default=1000000)
args = parser.parse_args()

for arg in vars(args):
    print('[%s] = ' % arg, getattr(args, arg))

splits = os.listdir(args.fold_A)

for sp in splits:
    img_fold_A = os.path.join(args.fold_A, sp)
    img_fold_B = os.path.join(args.fold_B, sp)
    img_list_A = os.listdir(img_fold_A)
    img_list_B = os.listdir(img_fold_B)

    num_imgs = min(args.num_imgs, len(img_list_A))
    print('split = %s, use %d/%d images' % (sp, num_imgs, len(img_list_A)))
    img_fold_AB = os.path.join(args.fold_AB, sp)
    if not os.path.isdir(img_fold_AB):
        os.makedirs(img_fold_AB)
    print('split = %s, number of images = %d' % (sp, num_imgs))
    for n in range(num_imgs):
        name_A = img_list_A[n]
        path_A = os.path.join(img_fold_A, name_A)
        name_B = img_list_B[n]
        path_B = os.path.join(img_fold_B, name_B)
        if os.path.isfile(path_A) and os.path.isfile(path_B):
            print('A:{}, B:{}'.format(path_A, path_B))
            name_AB = '{}_{}.png'.format(args.name_AB, str(n).zfill(4))
            path_AB = os.path.join(img_fold_AB, name_AB)
            im_A = cv2.imread(path_A, 1) # python2: cv2.CV_LOAD_IMAGE_COLOR; python3: cv2.IMREAD_COLOR
            im_B = cv2.imread(path_B, 1) # python2: cv2.CV_LOAD_IMAGE_COLOR; python3: cv2.IMREAD_COLOR
            im_AB = np.concatenate([im_A, im_B], 1)
            cv2.imwrite(path_AB, im_AB)
