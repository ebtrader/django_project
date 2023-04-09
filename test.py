import os

image_path = '/home/javed_tech/codingadventures.space/public/static/car.jpg'

def image_short(self):
    path = os.path.basename(self)
    return path

print(image_short(image_path))

