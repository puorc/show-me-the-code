# Project : show me the code
# Author : puorc
# iPhone 5 image resolution: 1136x640

from PIL import Image
import os


def resize(path, filename):
    WIDTH = 1136
    HEIGHT = 640
    size = []
    with Image.open(path + '/' + filename) as im:
        ratio = float(im.size[0]) / float(im.size[1])
        if im.size[0] <= WIDTH and im.size[1] <= HEIGHT:
            pass
        elif ratio > float(WIDTH) / float(HEIGHT):
            size = [WIDTH, int(float(WIDTH) / ratio)]
        else:
            size = [int(HEIGHT * float(ratio)), HEIGHT]
        nim = im.resize(tuple(size), Image.BILINEAR)
        nim.save(path + '/' + "resized" + filename)


imagetype = ('jpg', 'jpeg', 'bmp', 'png')
path = raw_input("Please input your path:")
for file in os.listdir(path):
    if file.endswith(imagetype):
        resize(path, file)
print 'Done!'
