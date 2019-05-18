import numpy as np
import matplotlib.pyplot as plt

def stretch(image):
    temp = image
    for i in range(image.shape[2]):
        minI    = np.min(image[:,:,i])
        maxI    = np.max(image[:,:,i])
        minO    = 0
        maxO    = 255

        temp[:,:,i] = (image[:,:,i]-minI)*(((maxO-minO)/(maxI-minI))+minO)
    
    return np.float32(temp)
