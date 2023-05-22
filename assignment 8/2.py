import os
import imageio

directory = './pics/'

image_files = [directory + file for file in os.listdir(directory) if file.endswith('.jpg')]

frame_duration = 0.1

with imageio.get_writer('animation.gif', mode='I', duration=frame_duration) as writer:
    for filename in image_files:
        image = imageio.imread(filename)
        writer.append_data(image)
