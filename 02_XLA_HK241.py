import cv2
import numpy as np
import random   #Import library

#Color pixel for each group
dataClass = np.array([[10, 20, 123], [40, 5, 96], [0, 0, 200], [200, 0, 0], [200, 200, 0], [0, 200, 0], [200, 0, 200], [0, 200, 200], [0,0,0], [100, 100, 100]])

#define class 
class pixel:
    def __init__(self, data, mean):
        self.data = data #pixel data
        self.mean = mean  #group

img = cv2.imread('img3.png')  #read image by openCV
row = img.shape[0]  #high
coulum = img.shape[1] #width
img1d = [] #image 1D

#use for transfer from 2D pixel three channel to 1D image 1 channel
for i in range(row):
    for j in range(coulum):
        R = int(img[i][j][0])
        G = int(img[i][j][1])
        B = int(img[i][j][2])
        temp = 256*256*R + 256*G + B
        pixelTemp = pixel(temp, 0)
        img1d.append(pixelTemp)
img1d = np.array(img1d)
leng = len(img1d)

cv2.imshow("image1", img)  #show origin image

NUMBER_OF_K = 5   #number of group
#data average of group
dataMean = range(NUMBER_OF_K)
dataMean = np.array(dataMean)
#number of pixel of group
numMean = range(NUMBER_OF_K)
numMean = np.array(numMean)
#total data all pixel of group
sumMean = range(NUMBER_OF_K)
sumMean = np.array(sumMean)
#distance from pixel to average of group
disMean = range(NUMBER_OF_K)
disMean = np.array(disMean)

#random initialiation for average of group
for i in range(NUMBER_OF_K):
    index = random.randint(0+1000*i, 1000 + 1000*i)
    dataMean[i] = img1d[index].data
    img1d[index].mean = i

print("khoi tao voi data group")
print(dataMean)

#Number of episo update average of group
for episo in range(20):
    for i in range(NUMBER_OF_K):
        numMean[i] = 0 #intialiation value before update
        sumMean[i] = 0
    for i in range(leng): #loop for each pixel of image
        for j in range(NUMBER_OF_K):   #calculate distance from current pixel to average of group
            disMean[j] = abs(img1d[i].data - dataMean[j])
        #print(disMean)
        group = np.argmin(disMean)  #find minimun distance from current pixel to average of group
        img1d[i].mean = group   #Update group for current pixel, group has been choised by minimun distance
        #print(group)
        sumMean[group] = sumMean[group] + img1d[i].data  #Plus pixel data to total data of group
        numMean[group] = numMean[group] + 1  #incraese number of pixel on group, which had been choised
    #print("so luong pha tu:")
    #print(numMean)
    #print("tong group")
    #print(sumMean)
    for i in range(NUMBER_OF_K): # loop for each group
        if (numMean[i] == 0):
            pass
        else:
            dataMean[i] = sumMean[i]/numMean[i] #recalculate average of group
    print("mean0: %d, mean1: %d, mean2: %d" %(dataMean[0], dataMean[1], dataMean[2]))
print(img1d[10].mean)
print(img1d[5000].mean)
print(img1d[20000].mean)
print("Number of group 1: %d, number of group 2: %d, number of group 3: %d" %(numMean[0], numMean[1], numMean[2]))
for r in range (row):  #loop for each row
    for c in range(coulum): #loop for each collunm
        i = r*coulum + c
        img[r][c][0] = dataClass[img1d[i].mean][0]
        img[r][c][1] = dataClass[img1d[i].mean][1]
        img[r][c][2] = dataClass[img1d[i].mean][2]  #update color of group for current pixel

cv2.imshow("image", img)  #show image after classified group
cv2.waitKey(0)
