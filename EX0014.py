# -*- coding: utf-8 -*-
from openpyxl import Workbook
from string import maketrans
from os import listdir


#  Make the input become a list to write to rows in Excel files
def format(string):
    rules = maketrans(',[]":\n', '      ')
    return filter(lambda x: x != '', string.translate(rules).split(' '))


filename = raw_input("Please input the file you need to write to excel : ")
wb = Workbook()
ws = wb.active
with open(filename, 'r') as file:
    for line in file:
        if line == '{\n' or line == '}':
            pass
        else:
            ws.append(format(line))
if 'out.xlsx' not in listdir('.'):
    wb.save("out.xlsx")
else:
    print 'File exists, please check'
