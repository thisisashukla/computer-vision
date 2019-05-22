
# coding: utf-8

# # Plot Utilities

# This notebook contains various functions required in the NN Curriculum code

# In[5]:


import matplotlib.pyplot as plt
from drawnow import drawnow, figure


# In[6]:


def get_points_of_label(data, labels, label):
    x_coords = [data[i][0] for i, x in enumerate(labels) if x[label] == 1]
    y_coords = [data[i][1] for i, x in enumerate(labels) if x[label] == 1]
    return x_coords, y_coords


# In[3]:


def draw_fig():
#     Plot the graph
    plt.clf() # Clear figure
    plt.grid(False) # Plot a grid
    plt.xlim(-1,1) # Set x-axis limits
    plt.ylim(-1,1) # Set y-axis limits

#     Generates our green line, that is, our learning line (Decision Boundary)
    plt.plot([xA, xB], [yA, yB], color='g', linestyle='-', linewidth=2)

#     Plot blue points
    x_coords, y_coords = get_points_of_color(x, -1)
    plt.plot(x_coords, y_coords, 'bo')

#     Plot red points
    x_coords, y_coords = get_points_of_color(x, 1)
    plt.plot(x_coords, y_coords, 'ro')

    plt.show()


# In[ ]:


def get_plot(data, labels, title):
    
#     Plot blue points
    x_coords, y_coords = get_points_of_label(data, labels, 0)
    plt.plot(x_coords, y_coords, 'bo')

#     Plot red points
    x_coords, y_coords = get_points_of_label(data, labels, 1)
    plt.plot(x_coords, y_coords, 'ro')
    plt.title(title)
    plt.show()


# In[ ]:


print('Plot Utilities Imported !')

