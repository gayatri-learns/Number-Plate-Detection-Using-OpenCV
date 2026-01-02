import cv2
import numpy as np

# Read image
img = cv2.imread('Car.jpg')
img = cv2.resize(img, None, fx=0.7, fy=0.7)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply filter and find edges
bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
edges = cv2.Canny(bfilter, 30, 200)

# Find contours
contours, _ = cv2.findContours(
    edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
contours = sorted(contours, key=cv2.contourArea, reverse=True)

# Find number plate contour
roi = None
for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.015 * perimeter, True)

    if len(approx) == 4:
        roi = approx
        break

if roi is None:
    print("Number plate not detected")
    exit()

# Convert ROI format
roi = np.array([roi], np.int32)

# Get bounding box
points = roi.reshape(4, 2)
x, y = points[:, 0], points[:, 1]

x1, x2 = np.min(x), np.max(x)
y1, y2 = np.min(y), np.max(y)

number_plate = img[y1:y2, x1:x2]
cv2.imshow("Number Plate", number_plate)

# Blur entire image
blurred_img = cv2.GaussianBlur(img, (51, 51), 30)

# Create mask
mask = np.zeros(img.shape[:2], dtype=np.uint8)
cv2.fillPoly(mask, roi, 255)

# Invert mask
mask_inv = cv2.bitwise_not(mask)

# Apply masks
bg = cv2.bitwise_and(blurred_img, blurred_img, mask=mask_inv)
fg = cv2.bitwise_and(img, img, mask=mask)

result = cv2.add(bg, fg)

cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
