from pathlib import Path
from PIL import Image, ImageColor


def change_colors(image_path, output_path, colors):
    with Image.open(image_path) as img:
        img = img.convert("RGBA")
        data = img.getdata()
        new_data = []
        for pixel in data:
            color_changed = False
            for color in colors:
                (original_color, new_color) = color
                if pixel[:3] == original_color:
                    new_data.append((*new_color, pixel[3]))
                    color_changed = True
                    break
            if not color_changed:
                new_data.append(pixel)

        img.putdata(new_data)
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        img.save(output_path)


def change_colors_tolerance(image_path, output_path, colors, tolerance):
    with Image.open(image_path) as img:
        img = img.convert("RGBA")
        data = img.getdata()
        new_data = []
        for pixel in data:
            color_changed = False
            for color in colors:
                (original_color, new_color) = color
                (r, g, b, a) = pixel
                if (r - tolerance) <= original_color[0] and original_color[0] <= (r + tolerance) and (g - tolerance) <= original_color[1] and original_color[1] <= (g + tolerance) and (b - tolerance) <= original_color[2] and original_color[2] <= (b + tolerance):
                    new_data.append((*new_color, pixel[3]))
                    color_changed = True
                    break
            if not color_changed:
                new_data.append(pixel)

        img.putdata(new_data)
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        img.save(output_path)
