# Project : show me the code
# Author : puorc

tmp = ''
with open('filtered_words.txt', 'r') as file:
    for line in file:
        tmp += line
filtered_words = tmp.split('\n')
content = raw_input('Please input your advice:')
try:
    filtered_words.index(content)
except ValueError:
    print 'Human Rights'
else:
    print 'Freedom'
