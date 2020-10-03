import os
from PIL import Image
from img2pdf import convert
from pdf2image import convert_from_path

images = convert_from_path('/home/belval/example.pdf')

for idx, img in enumerate(images):
    img.save('pdf_' + str(idx).zfill(len(str(len(images)))) + '.jpg', 'JPEG')
    
dl = os.listdir(".")
del dl[dl.index("asdf.py")]

file_name = open("out.pdf", "wb")
pdf_list = [] 

for f in dl:
    img = Image.open(f)
    if (int(f[-7:-4]) % 2) == 1:
        area = (125, 140, 1028+195, 1763)
    else:
        area = (231, 140, 1028+306, 1763)
    crop_img = img.crop(area)
    sizechange = crop_img.resize((1080,2316))
    sizechange.save(f)
    pdf_list.append(f)

pdf = convert(pdf_list)
file_name.write(pdf)
file_name.close()

