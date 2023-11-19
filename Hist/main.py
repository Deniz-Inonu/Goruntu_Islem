import numpy as np, cv2 as cv

img = cv.imread("image.jpg")
bins = np.zeros(256, np.int32)

for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):

        intensity = 0
        for k in range(0, len(img[i][j])):
            intensity += img[i][j][k]

        bins[intensity/3] += 1

print bins