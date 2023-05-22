import os
import imageio

# Set the directory containing the images
directory = './images/'

# Get a list of all the image files in the directory
image_files = [directory + file for file in os.listdir(directory) if file.endswith('.jpg')]

# Set the frame duration (in seconds)
frame_duration = 0.1

# Create the GIF
with imageio.get_writer('animation.gif', mode='I', duration=frame_duration) as writer:
    for filename in image_files:
        image = imageio.imread(filename)
        writer.append_data(image)
