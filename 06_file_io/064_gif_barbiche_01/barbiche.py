import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "barbiche.gif",
    save_all=True,
    append_images=[images[1]],
    duration=[2500, 125, 0],  # Dauer in ms pro Frame
    loop=0,
    disposal=2,
)
