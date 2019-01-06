import glob
import os.path
from PIL import Image
from resizeimage import resizeimage

for image in glob.glob('Stimuli_Colors/*.jpg'): #Glob does not take regular expressions but takes * which corresponds to 'anything' afterwards
    img = Image.open(image)
    img = resizeimage.resize_contain(img, [355, 355]) #resize contain does not crop your image but rescales it while keeping initial proportions to desired scale indicated by [ , ]
    img_output = 'Stimuli_Resize/'+ os.path.basename(image) # store new files in different folder but maintain name by adding basename of initial image path (e.g. initial imag path = 'Stimuli/Red.jpg', basename = 'Red.jpg')
    img.save(img_output, img.format) #save new image with new path and in same format as img (e.g. jpg)


for image in glob.glob('Stimuli_Shapes/*.jpg'): #Glob does not take regular expressions but takes * which corresponds to 'anything' afterwards
    img = Image.open(image)
    img = resizeimage.resize_contain(img, [355, 355]) #resize contain does not crop your image but rescales it while keeping initial proportions to desired scale indicated by [ , ]
    img_output = 'Stimuli_Resize/'+ os.path.basename(image) # store new files in different folder but maintain name by adding basename of initial image path (e.g. initial imag path = 'Stimuli/Red.jpg', basename = 'Red.jpg')
    img.save(img_output, img.format) #save new image with new path and in same format as img (e.g. jpg)
