import numpy as np
import matplotlib.pyplot as plt

def showImage(imgs, titles = None, title = None, scale = False):
    
    r, c = int(np.ceil(len(imgs)/5)), min(5, len(imgs)%5)
    if r > 1:
        f, ax = plt.subplots(r, c, figsize = (5*c, 5*r))
        for i in range(r):
            for j in range(c):
                if len(imgs[j].shape) == 3:
                    ax[i][j].imshow(imgs[i*c+j])
                else:
                    ax[i][j].imshow(imgs[i*c+j], cmap = 'gray')
                ax[i][j].axis(scale)
                if titles is not None:
                    ax[i][j].set_title(titles[i*c+j])
    elif c > 1:
        f, ax = plt.subplots(1, c, figsize = (5*c, 5))
        for j in range(c):
            if len(imgs[j].shape) == 3:
                ax[j].imshow(imgs[j])
            else:
                ax[j].imshow(imgs[j], cmap = 'gray')
            ax[j].axis(scale)
            if titles is not None:
                ax[j].set_title(titles[j])
    else:
        if len(imgs[0].shape) == 3:
            plt.imshow(imgs[0])
        else:
            plt.imshow(imgs[0], cmap = 'gray')
        plt.title(titles[0])
        plt.axis(scale)               
    
    plt.suptitle(title)
    plt.show()
            