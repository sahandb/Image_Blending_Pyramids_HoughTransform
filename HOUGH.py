import cv2
import numpy as np

# Read image
img = cv2.imread('hti.png', cv2.IMREAD_COLOR)
imgP = cv2.imread('hti.png', cv2.IMREAD_COLOR)
# Convert the image to gray-scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Find the edges in the image using canny detector
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
# Detect points that form a line
linesP = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=10, maxLineGap=250)
# Draw lines on the image
for line in linesP:
    x1, y1, x2, y2 = line[0]
    cv2.line(imgP, (x1, y1), (x2, y2), (0, 0, 255), 1)

lines = cv2.HoughLines(edges,1,np.pi/180,150)
for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    # x1 stores the rounded off value of (r * cos(theta) - 1000 * sin(theta))
    x1 = int(x0 + 1000 * (-b))
    # y1 stores the rounded off value of (r * sin(theta)+ 1000 * cos(theta))
    y1 = int(y0 + 1000 * a)
    # x2 stores the rounded off value of (r * cos(theta)+ 1000 * sin(theta))
    x2 = int(x0 - 1000 * (-b))
    # y2 stores the rounded off value of (r * sin(theta)- 1000 * cos(theta))
    y2 = int(y0 - 1000 * a)
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)

# Show result
cv2.imshow("Result Image HoughLinesP", imgP)
cv2.imshow("Result Image HoughLines", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
