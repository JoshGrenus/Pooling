# Big Data Programming Project 1
# Author: your name
import sys
import numpy as np


# @param: .pgm filename
# @return: a tuple (header, image array) # image array - numpy array
def pgmFileRead(fileName):
    h = w = col = row = 0
    file = open(fileName, 'r')
    img_header = []   # a place holder
    img = np.array([])   # a place holder
    imgTmp = []     #temp array to hold pmg values
    allVals = ""

    for line in file:
        if (len(line)<50):
            img_header.append(line.strip())
        else:
            break

    for item in img_header:
        if (item.startswith('#')):
            img_header.remove(item)
    pgmSize = img_header[1].split(" ")
    height = pgmSize[0], width = pgmSize[1]

    for line in file:
        imgTmp.append(line.strip())
    for x in imgTmp:
        allVals = allVals + " " + x
    imgTmp.clear()
    allVals = allVals.split(" ")
    allVals.remove('')
     
    for item in allVals:
        if (col == width):
            col = 0
            img = np.concatenate((img, imgTmp), axis=0)
            row += 1
            break
        imgTmp.append(item)
        col += 1
    
    print(allVals)
    print(img_header)
    print('\n')
    print(img)

    file.close()
    return img_header, img


# @param: image array; image header; name of the processed image
# return: NaN
def image_save(output_header, image_array, fileName):
    return None


# @param: image array, pool size
# @return: pooled array
def max_pooling(input_array, pool_size):
    pooled_array = np.array([])   # a place holder


    return pooled_array


# @param: image array, pool size
# @return: oil painted image array
def oil_painting(input_array, pool_size):
    oil_array = np.array([])  # a place holder

    return oil_array


def main():
    imgFileName, poolSize, part = sys.argv[1:]
    print (imgFileName)
    print (poolSize)
    print (part)
    pgmFileRead(imgFileName)


if __name__ == '__main__':
    main()
