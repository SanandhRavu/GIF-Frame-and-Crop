
import sys
from PIL import Image
import os

# if __name__ == "__main__":
#     print(f"Location of your images?:  {sys.argv[1]=}")
#     print(f"Desired destination of cropped images?:  {sys.argv[2]=}")
#     print(f"Left (x) coordinate:  {sys.argv[3]=}")
#     print(f"Top (y) coordinate:  {sys.argv[4]=}")
#     print(f"Right (x) coordinate:  {sys.argv[5]=}")
#     print(f"Bottom (y) coordinate:  {sys.argv[6]=}")

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


def multicrop(input, output, left, top, right, bottom):
    imageno = 1
    for path in os.listdir(input):
        full_path = os.path.join(input, path)
        if os.path.isfile(full_path):
            filelist.append(full_path)

    for i in filelist:
        image = read_image(i)
        image = crop(image, int(left), int(top), int(right), int(bottom))
        image.save(output + "/" + str(imageno) + '.png')
        imageno += 1


multicrop(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])

