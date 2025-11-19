import cv2, glob, os

print(glob.glob(f'12/2123/*.*'))
for zoom in range(12, 18):
    paths = glob.glob(f'{zoom}/*/*.png')
    print(len(paths))
    for path in paths:
        img = cv2.imread(path, 0)
        if ((img > 0) & (img < 255)).sum() == 0:
            os.remove(path)
            print('.', end='', flush=True)
        else:
            print(((img > 0) & (img < 255)).sum())