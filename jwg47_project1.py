# Big Data Programming Project 1
# Author: your name
import sys
import numpy as np
import math
import time
np.set_printoptions(threshold=sys.maxsize)



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
    global imgHeadPreRemove
    imgHeadPreRemove = []
    allVals = ""

    for line in file:                               #Loops through to get the header set up, stops after getting max num value.
        if ("255" in line):
           img_header.append(line.strip())
           break
        else:
           img_header.append(line.strip())
    imgHeadPreRemove = img_header
    for item in img_header:
        if not item.startswith("#"): 
            imgHeadTmp.append(item)
    img_header = imgHeadTmp

    pgmSize = img_header[1].split(" ")
    width = int(pgmSize[0])
    height = int(pgmSize[1])
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
    img = img.astype(int)
    file.close()

    return img_header, img


# @param: image array; image header; name of the processed image
# return: NaN
def image_save(output_header, image_array, fileName):
    periodIndex = fileName.index(".")
    if (imgType == "1"):
        newFileName = fileName[:periodIndex] + "_pooled_" + pS + fileName[periodIndex:]
    elif(imgType == "2"):
        newFileName = fileName[:periodIndex] + "_oil_painted" + fileName[periodIndex:]


    file = open (newFileName, "w")
    for line in output_header:
        file.write(line + "\n")
    file.close()
    with open(newFileName, "ab") as f:
        np.savetxt(f, image_array, fmt='%3.0f')
    


    return None


# @param: image array, pool size
# @return: pooled array
def max_pooling(input_array, pool_size):
    global newHeight
    global newWidth
    newHeight = int(math.ceil(height/int(pool_size)))
    newWidth = int(math.ceil(width/int(pool_size)))
    pooled_array = np.array([])   # a place holder
    pooled_array = np.zeros((newHeight, newWidth), dtype = int)
    for x in range(newHeight):
        for y in range(newWidth):
            xStart = x * int(pool_size)
            yStart = y * int(pool_size)
            xEnd = xStart + int(pool_size)
            yEnd = yStart + int(pool_size)
            vals = input_array[xStart:xEnd, yStart:yEnd]
            maxVal = vals.max()
            pooled_array[x][y] = maxVal

    return pooled_array


# @param: image array, pool size
# @return: oil painted image array
def oil_painting(input_array, pool_size):
    oil_array = np.zeros((height, width), dtype = int)
    for x in range (height):
        for y in range (width):
            xEnd = x + int(pool_size)
            yEnd = y + int(pool_size)
            vals = input_array[x:xEnd, y:yEnd]
            med = int(np.median(vals))
            oil_array[x:xEnd, y:yEnd] = med
            
    return oil_array


def main():
    imgFileName, poolSize, part = sys.argv[1:]
    header, imgNum = pgmFileRead(imgFileName)
    global pS
    global imgType
    pS = poolSize
    imgType = part
    if (part == "1"):
        pooledArray = max_pooling(imgNum, poolSize)
        header[1] = str(newWidth) + " " + str(newHeight)
        image_save(header, pooledArray, imgFileName)
    elif (part == "2"):
        pooledArray = oil_painting(imgNum, poolSize)
        image_save(header, pooledArray, imgFileName)
if __name__ == '__main__':
    main()