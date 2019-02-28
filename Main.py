from IOOperation import *
from Photo import *
from Slide import *

def main():

    parser = IOOperation()

    nameFile = "b_lovely_landscapes.txt"

    num, content = parser.read_file("./inputs/" + nameFile)

    photos = []
    slides = []

    for i in range(len(content)):
        photo = Photo(content[i][0], i, content[i][2:])
        photos.append(photo)

    photos = normalize(photos)
    index, slide = select_first_photo(photos)
    photos.pop(index)
    slides.append(slide)
    rest_photos = photos
    while len(rest_photos) > 0:
        iinFac , selected, index = slide.photo.bestIF(rest_photos)
        rest_photos.pop(index)
        slide = create_slide([selected])
        slides.append(slide)


    to_print = []
    for slide in slides:
        to_print.append(slide)

    parser.write_in_file(nameFile, to_print)


def select_first_photo(photos):
    return 0, create_slide([photos[0]])

def create_slide(photos):
    return Slide(photos)

def normalize(photos):
    verticals = list(filter(lambda x: x.pos == 'V', photos))
    all = list(filter(lambda x: x.pos == 'H', photos))
    while len(verticals) > 0:
        photo_1 = verticals.pop(0)
        photo_2 = verticals.pop(0)
        indexes = str(photo_1.index) + ' ' + str(photo_2.index)
        all.append(Photo("H", indexes, photo_1.tags + photo_2.tags))
    return all

if __name__ == '__main__':
    main()