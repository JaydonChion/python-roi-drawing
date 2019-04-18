import logging
import matplotlib.image as mpimg
import numpy as np
from matplotlib import pyplot as plt
import easygui
from roipoly import RoiPoly
import random
import brewer2mpl
import itertools
import sys
import json

logger = logging.getLogger(__name__)

logging.basicConfig(format='%(levelname)s ''%(processName)-10s : %(asctime)s '
                           '%(module)s.%(funcName)s:%(lineno)s %(message)s',
                    level=logging.INFO)

# Create image
print("please choose input image")
filename1 = easygui.fileopenbox()
num = easygui.enterbox("How many ROIs you want to draw?")
print("Processing...")
 

#with open('/home/sensetime/Desktop/roipoly.py/examples/coordinate.txt'', 'a') as f:

#    json.dump("image name: "+filename1,f, indent=4)
   
dpi = 10
img =mpimg.imread(filename1)

# Show the image
height, width, depth = img.shape
figsize = width / float(dpi), height / float(dpi)
fig = plt.figure(figsize=figsize)

plt.imshow(img, interpolation='nearest', cmap="Greys")
plt.colorbar()
plt.title("left click: line segment         right click: close region")
plt.show(block=False)

color_map = brewer2mpl.get_map('Accent', 'qualitative', 6)
colors = itertools.cycle(color_map.mpl_colors)



roinum=0
roiarray = []


while roinum<int(num):

# Let user draw ROI
    roiarray.append(RoiPoly(color=next(colors), fig=fig))
    

# Show the image with the ROIs
    fig = plt.figure(figsize=figsize)
    plt.imshow(img, interpolation='nearest', cmap="Greys")
    plt.colorbar()
    roiarray[roinum].display_roi()
    plt.title('draw ROI')
    plt.show(block=False)
    [x.display_roi() for x in roiarray]
        #[x.display_mean(img) for x in roiarray]
    roinum=roinum+1


print("done!")








