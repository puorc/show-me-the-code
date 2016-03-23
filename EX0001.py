# Project : show me the code
# Author : puorc
import random
import datetime


def get_sequence():
    sequence = []
    for i in range(ord('a'), ord("z") + 1):
        sequence.append(chr(i))
    sequence.append(str(datetime.datetime.now().day))
    sequence.append(str(datetime.datetime.now().hour))
    sequence.append(str(datetime.datetime.now().minute))
    sequence.append(str(datetime.datetime.now().month))
    return sequence


i = 1
j = 1
code = ""
print "the codes are:"
while i <= 200:
    while j <= 20:
        code += random.choice(get_sequence())
        j += 1
    print code
    j = 1
    code = ""
    i += 1
