# Project : show me the code
# Author : puorc
import re


class words_freq:
    def __init__(self, filename):
        self.__words_freq__ = {}
        with open(filename, 'r') as file:
            for line in file:
                self.__get_words_freq__(self.__get_words__(line))

    def __get_words__(self, line):
        return re.compile('\w+').findall(line)

    def __get_words_freq__(self, words):
        for i in words:
            if self.__words_freq__.has_key(i.lower()):
                self.__words_freq__[i.lower()] += 1
            else:
                self.__words_freq__[i.lower()] = 1

    def print_result(self):
        for item in self.__words_freq__:
            print "{0} : {1} times".format(item, self.__words_freq__[item])


filename = raw_input("Please input the path of yourfile:")
result = words_freq(filename)
result.print_result()
