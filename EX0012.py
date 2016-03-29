# Project : show me the code
# Author : puorc

def replacer(string):
    tmp = ''
    with open('filtered_words.txt', 'r') as file:
        for line in file:
            tmp += line
    filtered_words = tmp.split('\n')
    tmp = string
    mixed_len = lambda x: len(x) if x.isalpha() else len(x) / 3
    for i in filtered_words:
        try:
            pos = string.index(i)
        except ValueError:
            pass
        else:
            tmp = tmp[0:pos] + '*' * mixed_len(i) + tmp[pos + len(i):]
    return tmp


content = raw_input('Please input your advice:')
print replacer(content)
