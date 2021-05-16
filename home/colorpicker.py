
# importing modules
import urllib.request
from PIL import Image

# this is not used here
def compute_average_image_color(img):
    width, height = img.size

    r_total = 0
    g_total = 0
    b_total = 0

    count = 0
    for x in range(0, width-1):
        for y in range(0, height-1):
            band = img.getpixel((x,y))
            r = band[0]
            g = band[1]
            b = band[2]
            r_total += r
            g_total += g
            b_total += b
            count += 1
    

    return '#%02x%02x%02x' % (r_total//count, g_total//count, b_total//count)

def compute_border_image_color(img):
    width, height = img.size

    r_total = 0
    g_total = 0
    b_total = 0

    count = 0
    for x in range(0, width-1):
        band = img.getpixel((x,0))
        r=band[0]
        g=band[1]
        b=band[2]
        r_total += r
        g_total += g
        b_total += b
        count += 1
    for x in range(0, width-1):
        band = img.getpixel((x,height-1))
        r=band[0]
        g=band[1]
        b=band[2]
        r_total += r
        g_total += g
        b_total += b
        count += 1
    for y in range(0, height-1):
        band = img.getpixel((0,y))
        r=band[0]
        g=band[1]
        b=band[2]
        r_total += r
        g_total += g
        b_total += b
        count += 1
    for y in range(0, height-1):
        band = img.getpixel((width-1,y))
        r=band[0]
        g=band[1]
        b=band[2]
        r_total += r
        g_total += g
        b_total += b
        count += 1
    return '#%02x%02x%02x' % (r_total//count, g_total//count, b_total//count)
# I have used this library for the final dominant_color
from colorthief import ColorThief

def finding_dominating_color(imgurl):
    urllib.request.urlretrieve(imgurl,"1.jpeg")
    img = Image.open("1.jpeg")
    average_color=compute_average_image_color(img)
    color_thief = ColorThief('1.jpeg')
    # get the dominant color
    dominant_color = color_thief.get_color(quality=1)
    print(average_color)
    print(dominant_color,"using color theif")
    return '#%02x%02x%02x' %dominant_color

def finding_border_color(imgurl):
    urllib.request.urlretrieve(imgurl,"1.jpeg")
    img = Image.open("1.jpeg")
    border_color=compute_border_image_color(img)
    print(border_color)
    return border_color


