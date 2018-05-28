import os, sys
from PIL import Image

size = 128, 128

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"

files = {'t-shirt.jpg': 'IMG_20180430_085634.jpg',
         'sponsors.jpg': 'IMG_20180430_085554.jpg'}

for out_file, in_file in files.items():

    im = Image.open(in_file)
    height = im.size[1]
    width = im.size[0]

    new_height = 300
    new_width = int(new_height * width / height)

    try:

        im = im.resize((new_width, new_height))
        im.save(out_file, "JPEG")
    except IOError:
        print("cannot create thumbnail for '%s'" % infile)
