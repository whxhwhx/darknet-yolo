from os import walk, path
import cv2
import os


if __name__ == "__main__":
    if not os.path.exists("rename_imgs"):
        os.mkdir("rename_imgs")
    rootdir = os.getcwd() + '/zheng/'
    resize_dir = os.getcwd() + '/rename_imgs/'
    print(rootdir)
    print(resize_dir)
    i = 1
    for root, dirs, files in walk(rootdir, topdown=True):
        for file in files:
            img = cv2.imread(os.path.join(root, file))
            # resize_img = cv2.resize(img, (224, 224))
            cv2.imwrite(os.path.join(resize_dir, ('%09d' % i + '.jpg')), img)
            i += 1

