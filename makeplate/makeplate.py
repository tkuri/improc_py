import numpy as np
import cv2

if __name__ == '__main__':
    buf = np.zeros((192, 192, 3),  dtype=np.int)

    for i in range(0, 256):
        buf[:] = i
        ofname = 'plate' + str(i).zfill(3) + '.png'
        cv2.imwrite(ofname, buf)

