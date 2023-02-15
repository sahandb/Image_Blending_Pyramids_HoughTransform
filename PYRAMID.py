import cv2
import numpy as np
import copy

apple = cv2.imread('apple.png')
orange = cv2.imread('orange.png')

apple = cv2.resize(apple, (orange.shape[1], orange.shape[0]))
# orange = cv2.resize(orange, (apple.shape[1], apple.shape[0]))

mask = np.zeros_like(apple)
# mask = np.zeros_like(apple,dtype='float32')
for col in range(apple.shape[0]):
    for row in range(apple.shape[1]):
        if col <= row:
            mask[col, row, :] = 1
mask2 = 1 - mask

# generate Gaussian pyramid for apple
apple_copy = copy.copy(apple)
gp_apple = [apple_copy]
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

# generate Gaussian pyramid for orange
orange_copy = copy.copy(orange)
gp_orange = [orange_copy]
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# generate Gaussian pyramid for Mask
mask_copy = copy.copy(mask)
gp_mask = [mask_copy]
for i in range(6):
    mask_copy = cv2.pyrDown(mask_copy)
    gp_mask.append(mask_copy)


# generate Laplacian Pyramid for apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5, 0, -1):
    size = (gp_apple[i - 1].shape[1], gp_apple[i - 1].shape[0])
    gaussian_expanded = cv2.pyrUp(gp_apple[i], dstsize=size)
    laplacian = cv2.subtract(gp_apple[i - 1], gaussian_expanded)
    lp_apple.append(laplacian)

# generate Laplacian Pyramid for orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range(5, 0, -1):
    size = (gp_orange[i - 1].shape[1], gp_orange[i - 1].shape[0])
    gaussian_expanded = cv2.pyrUp(gp_orange[i], dstsize=size)
    laplacian = cv2.subtract(gp_orange[i - 1], gaussian_expanded)
    lp_orange.append(laplacian)

# generate Laplacian Pyramid for mask
mask_copy = gp_mask[5]
lp_mask = [mask_copy]
for i in range(5, 0, -1):
    size = (gp_mask[i - 1].shape[1], gp_mask[i - 1].shape[0])
    gaussian_expanded = cv2.pyrUp(gp_mask[i], dstsize=size)
    laplacian = cv2.subtract(gp_mask[i - 1], gaussian_expanded)
    lp_mask.append(laplacian)



apple_orange_pyramid = []

n = 0
for apple_lap, orange_lap, mask_lap in zip(lp_apple, lp_orange, lp_mask):
    n += 1
    cols, rows, ch = apple_lap.shape
    # laplacian = np.hstack((apple_lap[:, 0:int(cols / 2)], orange_lap[:, int(cols / 2):]))
    mask_lap2 = 1 - mask_lap
    laplacian = (apple_lap * mask_lap + orange_lap * mask_lap2)
    # laplacian = np.sum(np.dot(apple_lap, mask_lap), np.dot(orange_lap, mask_lap2))
    apple_orange_pyramid.append(laplacian)

# now reconstruct
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
    size = (apple_orange_pyramid[i].shape[1], apple_orange_pyramid[i].shape[0])
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct, dstsize=size)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv2.imshow("apple", apple)
cv2.imshow("orange", orange)
cv2.imshow("apple_orange_reconstruct", apple_orange_reconstruct)
# cv2.imshow("apple_orange_reconstruct", np.array(apple_orange_reconstruct,dtype=np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
