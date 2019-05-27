import numpy as np
import matplotlib.pyplot as plt

def stretch(image, mode = 'linear'):
    temp = image.copy()
    if(len(temp.shape) == 3):
        for i in range(image.shape[2]):
            minI    = np.min(image[:,:,i])
            maxI    = np.max(image[:,:,i])
            minO    = 0
            maxO    = 255

            temp[:,:,i] = (image[:,:,i]-minI)*(((maxO-minO)/(maxI-minI))+minO)
    else:
        minI    = np.min(image)
        maxI    = np.max(image)
        minO    = 0
        maxO    = 255

        temp = (image-minI)*(((maxO-minO)/(maxI-minI))+minO)
    return temp
