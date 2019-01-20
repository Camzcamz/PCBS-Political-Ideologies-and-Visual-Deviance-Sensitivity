import glob
import os.path
from PIL import Image
from resizeimage import resizeimage

def Rescale_Stim (Stim_To_Rescale_Path):
  for image in glob.glob(Stim_To_Rescale_Path):
      img = Image.open(image)
      img = resizeimage.resize_contain(img, [355, 355]) #resize contain does not crop your image but rescales it while keeping initial proportions to desired scale indicated by [ , ]
      img_output = 'Stimuli_Resize/'+ os.path.basename(image) # store new files in different folder but maintain name by adding basename of initial image path (e.g. initial imag path = 'Stimuli/Red.jpg', basename = 'Red.jpg')
      img.save(img_output, img.format)

Rescale_Stim ('Stimuli_Colors/*.jpg')
Rescale_Stim ('Stimuli_Shapes/*.jpg')
