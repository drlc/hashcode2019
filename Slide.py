from functools import reduce
from Photo import *

class Slide(object):

    def __init__(self, photos):
        if len(photos) > 1:
            self.indexes = str(photos[0].index) + ' ' + str(photos[1].index)
            self.photo = Photo("V", self.indexes, photos[0].tags + photos[1].tags)
        else :
            self.indexes = str(photos[0].index)
            self.photo = photos[0]

    def __str__(self):
        return self.indexes