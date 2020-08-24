
from PIL import Image
import os


filelist = []


def read_image(path):
    try:
        image = Image.open(path)
        return image
    except Exception as e:
        print(e)


def crop(image, left, top, right, bottom):
    cropped = image.crop((left, top, right, bottom))
    return cropped

d = input('Location of your images?: ')
e = input('Where do you want to save your images?: ')
l = input('Left (x) coordinate: ')
t = input('Top (y) coordinate: ')
r = input('Right (x) coordinate: ')
b = input('Bottom (y) coordinate: ')

def multicrop(input, output, left, top, right, bottom):
    imageno = 1
    for path in os.listdir(input):
        full_path = os.path.join(input, path)
        if os.path.isfile(full_path):
            filelist.append(full_path)

    for i in filelist:
        image = read_image(i)
        image = crop(image, left, top, right, bottom)
        image.save(output + str(imageno) + '.png')
        imageno += 1

multicrop(d, e, l, t, r, b)
