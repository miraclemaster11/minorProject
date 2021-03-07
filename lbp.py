import cv2
# import lbph as lr
import numpy as np
import matplotlib.pyplot as plt


def convert_binary(clockwise_binary_num):
    required_number = clockwise_binary_num[::-1]
    summation = 0
    power = 0
    for char in required_number:
        add_element = int(char) * (2 ** power)
        summation = summation + add_element
        power += 1
    return summation
#   myimage = cv2.imread(image_path)
#   lbp_converted = convert_to_lbp(myimage)
# lbp_converted is the expected output equivalent to converted lbp
def convert_to_lbp(image):
    """
    param: image array including color pixel
    return: Lbp array for corresponding picture
    """
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imgLBP = np.zeros_like(gray_image)
    neighbour = 3
    for ih in range(0, image.shape[0] - neighbour + 1):
    # print("new row" + str(ih))
        for iw in range(0, image.shape[1] - neighbour + 1):
            window = gray_image[ih:ih + neighbour, iw:iw + neighbour]
            # print("new column" + str(iw))
            center = window[1, 1]
            # print(center)
            #  creates 3x3 sliding window
            # print(window)
            # img01 = (window >= center) * 1.0
            # img01_vector = img01.flatten()
            # for rows in range(3):
            #     for column in range(3):
            #         if window[rows]
            clockwise_binary = ""
            if window[0, 0] < center:
                d0 = 0
            else:
                d0 = 1
            if window[0, 1] < center:
                d1 = 0
            else:
                d1 = 1
            if window[0, 2] < center:
                d2 = 0
            else:
                d2 = 1
            if window[1, 2] < center:
                d3 = 0
            else:
                d3 = 1
            if window[2, 2] < center:
                d4 = 0
            else:
                d4 = 1
            if window[2, 1] < center:
                d5 = 0
            else:
                d5 = 1
            if window[2, 0] < center:
                d6 = 0
            else:
                d6 = 1
            if window[1, 0] < center:
                d7 = 0
            else:
                d7 = 1
            clockwise_binary = str(d0) + str(d1) + str(d2) + str(d3) + str(d4) + str(d5) + str(d6) + str(d7)
            decimal_equivalent = convert_binary(clockwise_binary)
            imgLBP[ih + 1, iw + 1] = decimal_equivalent
    return imgLBP


'''
image = cv2.imread("kangaroo.jpg")
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# trained_face_recognizer = lr.train_lbph(img)
# print("done")
# numpy.save('trainedrecordnum.npy', trained_face_recognizer)
# print(gray_img)
# print(gray_img.shape)
# (s1, s2) = gray_img.shape
# print(s1)
# imge = numpy.zeros()
# images_processed = numpy.zeros((5, 5))
# images_processed = numpy.zeros((s1, (s2-4)))
# print(images_processed)
# window = 3
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# resized_image = cv2.resize(gray_image, (20, 20))
# plt.imshow(gray_image, "gray")
# plt.show()
# print(gray_image)
imgLBP = np.zeros_like(gray_image)
# print(imgLBP)
neighbour = 3

# print(image.shape)
for ih in range(0, image.shape[0] - neighbour + 1):
    # print("new row" + str(ih))
    for iw in range(0, image.shape[1] - neighbour + 1):
        window = gray_image[ih:ih + neighbour, iw:iw + neighbour]
        # print("new column" + str(iw))
        center = window[1, 1]
        # print(center)
        #  creates 3x3 sliding window
        # print(window)
        # img01 = (window >= center) * 1.0
        # img01_vector = img01.flatten()
        # for rows in range(3):
        #     for column in range(3):
        #         if window[rows]
        clockwise_binary = ""
        if window[0, 0] < center:
            d0 = 0
        else:
            d0 = 1
        if window[0, 1] < center:
            d1 = 0
        else:
            d1 = 1
        if window[0, 2] < center:
            d2 = 0
        else:
            d2 = 1
        if window[1, 2] < center:
            d3 = 0
        else:
            d3 = 1
        if window[2, 2] < center:
            d4 = 0
        else:
            d4 = 1
        if window[2, 1] < center:
            d5 = 0
        else:
            d5 = 1
        if window[2, 0] < center:
            d6 = 0
        else:
            d6 = 1
        if window[1, 0] < center:
            d7 = 0
        else:
            d7 = 1
        clockwise_binary = str(d0) + str(d1) + str(d2) + str(d3) + str(d4) + str(d5) + str(d6) + str(d7)
        decimal_equivalent = convert_binary(clockwise_binary)
        imgLBP[ih + 1, iw + 1] = decimal_equivalent
plt.imshow(imgLBP, "gray")
plt.show()
'''
