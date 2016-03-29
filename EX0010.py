# Project : show me the code
# Author : puorc
import random
from PIL import Image, ImageFont, ImageColor, ImageDraw


class verification_code:
    def __init__(self):
        self.__base__ = Image.new('RGB', (240, 60), color=ImageColor.getrgb('grey'))
        self.__text__ = Image.new('RGB', (240, 60), color=ImageColor.getrgb('grey'))
        self.__colors__ = ['red', 'green', 'blue', 'purple', 'orange', 'black']
        self.__string__ = self.__get_random_string__()

    def __get_random_string__(self):
        alphabet = []
        for i in range(ord('A'), ord('Z') + 1):
            alphabet.append(chr(i))
        for i in range(ord('a'), ord('z') + 1):
            alphabet.append(chr(i))
        for i in range(0, 10):
            alphabet.append(str(i))
        string = ""
        i = 0
        while i < 4:
            string += random.choice(alphabet)
            i += 1
        return string

    def __draw__(self):
        draw_base = ImageDraw.Draw(self.__base__)
        i = 0
        j = 0
        while i <= 240:
            while j <= 60:
                draw_base.point((i, j), fill=ImageColor.getrgb(random.choice(self.__colors__)))
                j += 2
            i += 2
            j = 0
        font = ImageFont.truetype('yahei.ttf', size=40)
        draw_text = ImageDraw.Draw(self.__text__)
        i = 0
        while i < 4:
            draw_text.text((35 + random.randint(-2, 2) + 55 * i, 9 + random.randint(-2, 2)),
                           list(self.__string__)[i] + " ",
                           fill=ImageColor.getrgb(random.choice(self.__colors__)), font=font)
            i += 1
        return Image.blend(self.__base__, self.__text__, 0.3)

    @property
    def image_object(self):
        return self.__draw__()

    @property
    def content(self):
        return self.__string__

    def show(self):
        self.image_object.show()

    def save(self, filename):
        self.image_object.save(filename)
