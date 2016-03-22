# Project : show me the code
# Author : puorc
# Mac OS X + Pycharm + Pillow

from PIL import Image, ImageDraw, ImageFont


def getfilename(string):
    completefilename = []
    if string.find("\\") == -1 and string.find("/") == -1:
        completefilename.append(string)
    elif string.find("\\") != -1:
        completefilename = string.split("\\")
    else:
        completefilename = string.split("/")
    return tuple(completefilename[-1].split("."))


print "Please input the filepath\n#"
filename = raw_input()
print "Please input the number\n#"
num = raw_input()
try:
    im = Image.open(filename)
except IOError:
    print "Can't open the file."
font = ImageFont.truetype("yahei.ttf", 30)
width = im.size[0]
height = im.size[1]
draw = ImageDraw.Draw(im)
draw.text((width - 50, 10), num, fill="#ff0000", font=font)
imname = getfilename(filename)[0] + "-modified"
imtype = getfilename(filename)[1]
im.save(imname + "." + imtype)
print "Success! "
