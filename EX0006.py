# Project : show me the code
# Author : puorc

import os

path = raw_input("Please input your path:")
count_of_comments = 0
count_of_blanks = 0
count_of_codes = 0
for filename in os.listdir(path):
    if filename.endswith('.py') == True:
        with open(path + '/' + filename) as _file:
            for line in _file:
                if line == '\n':
                    count_of_blanks += 1
                elif line.startswith('#'):
                    count_of_comments += 1
                else:
                    count_of_codes += 1
print "The numbers of lines of code:{0}\nThe numbers of lines of comments:{1}\nThe numbers of lines of blanks:{2}\n".format(
    count_of_codes, count_of_comments, count_of_blanks)
