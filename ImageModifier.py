import numpy as np
from PIL import Image, ImageOps

class Convolution:
    def __init__(self):
        #edge detection
        self.filters = (np.array([[-1, -1, -1],
                 [-1, 8, -1],
                 [-1, -1, -1]]) ,
        #box Blur
        np.array([[1/9,1/9,1/9],
                        [1/9,1/9,1/9],
                        [1/9,1/9,1/9]]) ,
        #guassian Blur 
        np.array([[1/16,1/8,1/16],
                                [1/8,1/4,1/8],
                                [1/16,1/8,1/16]]),
        #sharpening
        np.array([[-1,-1,-1],
                            [-1,9,-1],
                            [-1,-1,-1]]))
    def getPath(self):
        return input("Please enter the path to your image: ")
    
    def getChoice(self):
        choice = input("1) For edge detection\n2) For Box Blur\n3) For guassianBlur\n4) For sharpening: ")
        return self.filters[int(choice)-1]
    
    def convertImage(self, path):
        img = Image.open(path)
        greyScale = ImageOps.grayscale(img)
        greyScale.show()
        return np.asarray(greyScale)
    
    def convertToImage(self,imageArray):
        image = Image.fromarray(imageArray)
        image.show()
    


    def convolution(self,arr,kernal):
            i = 0
            j = 0
            Finalarr = []
            rows, cols = arr.shape
            for i in range(len(arr)):
                for j in range(len(arr[0])):
                    #index map for out of range indices
                    indices = [
                        (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                        (i, j - 1), (i, j), (i, j + 1),
                        (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)
                    ]
                    # getting 3x3 array from input array to preform convolution
                    newarr = np.array([
                        arr[x][y] if 0 <= x < rows and 0 <= y < cols else 0 for x , y in indices
                    ])
                    #preforming convolution using dot product of kernal and 3x3 section of input array
                    result = np.dot(np.reshape(newarr, newshape=(3,3)), kernal)
                    Finalarr.append(np.sum(result[result != 0]))
            return np.array(Finalarr)
    #main program
    def doConvolution(self):
        print("Convolute: Liam Roberts\n\n")
        path = self.getPath()
        kernal = self.getChoice()
        arr = self.convertImage(path)
        convolutionArr = self.convolution(arr, kernal)
        convolutionArr = convolutionArr.reshape(arr.shape[0], arr.shape[1])
        self.convertToImage(convolutionArr)

newConv = Convolution()
newImage = newConv.doConvolution()
