# Big Data Programming Project 1
# Author: your name
import sys
import numpy as np
import math


# @param: .pgm filename
# @return: a tuple (header, image array) # image array - numpy array
def pgmFileRead(fileName):
    global height, width
    height = width = col = row = k =0
    word = let = ""
    y = 5
    file = open(fileName, 'r')
    img_header = []   # a place holder
    img = np.array([])   # a place holder
    imgTmp = []     #temp array to hold pmg values
    imgHeadTmp = []
    allVals = ""

    for line in file:                               #Loops through to get the header set up, stops after getting max num value.
        if ("255" in line):
           img_header.append(line.strip())
           break
        else:
           img_header.append(line.strip())

    for item in img_header:
        if not item.startswith("#"):  # Use != to check for inequality
            imgHeadTmp.append(item)
    img_header = imgHeadTmp

    pgmSize = img_header[1].split(" ")
    height = int(pgmSize[0])
    width = int(pgmSize[1])
    img = np.zeros((height,width))

    for line in file:

        imgTmp.append(line.strip())
        y += 1

    for x in imgTmp:
        allVals = allVals + " " + x

    imgTmp.clear()
    allVals = allVals.split(" ")
    allVals.remove('')
    img = np.zeros((height,width))
    img = np.array(allVals)
    img = img.reshape(height,width)

    file.close()
    return img_header, img


# @param: image array; image header; name of the processed image
# return: NaN
def image_save(output_header, image_array, fileName):
    return None


# @param: image array, pool size
# @return: pooled array
def max_pooling(input_array, pool_size):
    newHeight = int(math.ceil(height/int(pool_size)))
    newWidth = int(math.ceil(width/int(pool_size)))
    pooled_array = np.array([])   # a place holder
    print (newHeight, newWidth)
    pooled_array = np.zeros((newHeight, newWidth),dtype = int)
    print (pooled_array)

    return pooled_array


# @param: image array, pool size
# @return: oil painted image array
def oil_painting(input_array, pool_size):
    oil_array = np.array([])  # a place holder

    return oil_array


def main():
    imgFileName, poolSize, part = sys.argv[1:]

    header, imgNum = pgmFileRead(imgFileName)

    max_pooling(imgNum, poolSize)
    

if __name__ == '__main__':
    main()