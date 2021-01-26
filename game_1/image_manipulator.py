from PIL import Image
import os


output_size = (1300, 720)

i = Image.open('1624.jpg')
i.thumbnail(output_size)
i.show()
i.save('background.png')