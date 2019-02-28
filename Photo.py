import string

class Photo(object):

    def __init__(self, pos, index, tags):
        self.pos = pos
        self.index = index
        self.tags = tags


    def bestIF(self, photos):
        #(if, photo, indice)
        print('bestIF')
        max1 = (0, 0, 0)
        for i in range(len(photos)):
            tempIf = self.findIF(photos[i])
            if tempIf > max1[0]:
                max1 = (tempIf, photos[i], i)
        print('found bestIf')
        return max1

    def findIF(self, otherPhoto):
        print('fIF')
        mine = 0
        their = 0
        common = 0
        otherTags = otherPhoto.tags
        for tag in self.tags:
            if tag in otherTags:
                common =+ 1
            else :
                mine =+ 1
        if common == 0 or mine == 0:
            print('endf fIF')
            return 0
        for tag in otherTags:
            if tag not in self.tags:
                their =+ 1
        print('endf fIF')
        return min(mine, their, common);

    def __str__(self):
        return 'Photo: ' + str(self.index) + ' ' + self.pos + ' - tags: ' + ''.join(self.tags)