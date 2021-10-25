from PIL import Image, ImageDraw
import random
import hashlib
import string
from scipy import spatial

#Generate a random polygon with n sides
def generate_random_polygon(n: int, x_px_range: int, y_px_range: int, padding: int):
    r_points = []
    for _ in range(n):
        r_points.append((random.randint(padding, x_px_range - padding), random.randint(padding, y_px_range - padding)))
    return r_points

def draw_points(draw: ImageDraw, points: [], num_lines: int):
    for i in range(num_lines):

        if i == len(points) - 1:
            p2 = points[0]

        else:
            p2 = points[i+1]

        line_xy = (points[i], p2)
        line_colour = (255, 255, 255)
        draw.line(line_xy, fill=line_colour, width = 2)

def normalise(x: int) -> int:
    x = x**5
    x = x // 1028
    x = x%500
    return x

def generate_hash_string_md5(s: str):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

def generate_hash_string_sha256(s: str):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

def generate_hash_string_sha512(s: str):
    return hashlib.sha512(s.encode('utf-8')).hexdigest()

def generate_hash_string_sha1(s: str):
    return hashlib.sha1(s.encode('utf-8')).hexdigest()

def save_image_md5(image, str):
    image.save("art/md5/{filename}.png".format(filename = str))

def save_image_sha1(image,str):
    image.save("art/sha1/{filename}.png".format(filename = str))

def save_image_sha256(image,str):
    image.save("art/sha256/{filename}.png".format(filename = str))

def save_image_sha512(image,str):
    image.save("art/sha512/{filename}.png".format(filename = str))

def str_generator(size = 10, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def make_image(hash_str: str):
    #Create a new image
    image_size = 512
    image_padding = 12
    image_bg_colour = (0, 0, 0)
    image = Image.new(mode="RGB", size=(image_size, image_size), color=image_bg_colour)

    #Drawing
    draw = ImageDraw.Draw(image)

    points = []

    line_colour = (255,255,255)

    for i in range(0, len(hash_str), 2):
        x = normalise(ord(hash_str[i]))
        y = normalise(ord(hash_str[i+1]))

        p1 = (image_size/2 , image_size/2)
        p2 = (x, y)
        line_xy = (p1, p2)
        points.append(p2)

        draw.line(line_xy, fill = line_colour, width =  2)


    for i in range(len(points) - 1):

        kd_tree = spatial.KDTree(points)
        _, q = kd_tree.query([points[i]], k=3)
        p2 = points[q[0][1]]
        p3 = points[q[0][2]]
        line_xy = (points[i], p2)
        line_xy2 = (p2, p3)

        draw.line(line_xy, fill = line_colour, width = 2)
        draw.line(line_xy2, fill = line_colour, width = 2)

    #Save image
    #image.save("art/{filename}.png".format(filename = r_str))
    #image.save("art/{filename}.png".format(filename = hash_str))
    return image


#Generate an image
def generate(r_str):
    print("Generating")
    #Generating the different hashes
    hash_str_md5 = generate_hash_string_md5(r_str)

    hash_str_sha1 = generate_hash_string_sha1(r_str)

    hash_str_sha256 = generate_hash_string_sha256(r_str)

    hash_str_sha512 = generate_hash_string_sha512(r_str)

    #make_image(hash_str_md5)
    #save_image_md5(make_image(hash_str_md5), r_str)

    #save_image_sha1(make_image(hash_str_sha1), r_str)

    #save_image_sha256(make_image(hash_str_sha256), r_str)

    #save_image_sha512(make_image(hash_str_sha512), r_str)

    image = make_image(hash_str_sha1)
    image.save("test.png")




# --------------------------------------------------- #
# This program is exploring how different
# hash functions can be visualised using
# a unique type of art generation, by
# drawing lines based on the hash that
# each function will create given the
# same string input. This program uses
# the hashlib library to implement the
# different hash functions and uses PIL
# in order to create the image, draw the
# lines and save the image. Each character
# of the hash is converted into a co-ordinate
# that will be used by the program to draw
# the lines. It uses the normalise() function
# to make sure the range of numbers from the
# hash will make an even distribution across
# the canvas. Then, when the lines are plotted
# the program will draw a line between each
# nearest neighbour and another line between the
# nearest neighbours nearest neighbour. I used the
# spatial import from the scipy library to calculate
# the nearest neighbours by putting the co-ordinates
# into a KDTree. The results from this program are
# very interesting in my opinion and a slight change
# in the normalise() function calculcation can
# change the outcome so drastically.
# In the current state of the program it only deals
# with a black background and white lines. I am still
# considering how to compute this information for each
# hash. Potentially having a different colour for
# each line wouldn't look very good so I need to
# think about this some more. Maybe computing a start colour
# and an end colour and having a gradient for the background.
# Not sure how to deal with the line colours yet, although
# I quite like the black and white for now it has a lot of
# room for creativity with different colours.
# I will update the code when I have come up with a good idea.
# Need to research colour spectrum calculations more because RGB
# would probably make for some boring/silly outcomes.
# --------------------------------------------------- #

if __name__ == "__main__":
    r_str = str_generator()
    generate(r_str)
