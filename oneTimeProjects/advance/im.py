import os
from PIL import Image

os.chdir("C:\\Users\\SG704\\Desktop\\web\\img")

img1 = Image.open("1-2-wink-emoji-png.png")
print(img1.size)
print(img1.format_description)
print(img1.format)
print(img1.filename)
#img1.show()
img1.crop((335, 345, 505, 520)).show()
#cim.save("tc.png")
'''
# Create Image
img2 = Image.new("RGBA", (1, 1), "purple")
img2.save("1pixpurple.png")
'''