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
import cv2
import os


msg = "Please choose direction"
title = "Choose roi direction"
choices = ["Up","Down"]

logger = logging.getLogger(__name__)

logging.basicConfig(format='%(levelname)s ''%(processName)-10s : %(asctime)s '
                           '%(module)s.%(funcName)s:%(lineno)s %(message)s',
                    level=logging.INFO)

# Create image
print("please choose input video")
filename1 = easygui.fileopenbox()
num = easygui.enterbox("How many ROIs you want to draw?")
print("Processing...")
 

#with open('/home/jetherng/roipoly.py/examples/coordinate.json', 'a') as f:

#    json.dump("image name: "+filename1,f, indent=4)
   
dpi = 10

vidcap = cv2.VideoCapture(filename1)
success,image = vidcap.read()

print(success)
cv2.imwrite("frame.jpg", image)
img =mpimg.imread("frame.jpg")

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

#    with open('/home/jetherng/roipoly.py/examples/coordinate.json', 'a') as f:
 #       f.write("\n")
#        json.dump("roi "+str(roinum),f)
# Let user draw ROI
    roiarray.append(RoiPoly(color=next(colors), fig=fig))

#choose direction
    var = easygui.choicebox(msg,title,choices)
    with open('/home/sensetime/Desktop/roipoly.py/examples/coordinate.txt', 'a') as f:
        f.write(var+"\n")
    

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
	

path = os.getcwd()
os.remove(os.path.join(path,"frame.jpg"))

#fig.savefig("frame.jpg",dpi=1500, bbox_inches='tight')
print("done!")








