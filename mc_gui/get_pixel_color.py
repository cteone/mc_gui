from PIL import Image

def get_pixel_color(image_path,x,y):
  with Image.open(image_path) as img:
    img = img.convert("RGBA")

    pixel_color = img.getpixel((x,y))
  return pixel_color