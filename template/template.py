import numpy as np
import cv2

if __name__ == '__main__':
    buf = np.zeros((128, 128, 3),  dtype=np.int)

    cv2.imwrite('test.png', buf)

