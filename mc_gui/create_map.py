from PIL import ImageColor

import json


def create_map(original, new):
    color_pairs = [(ImageColor.getrgb(original[key]),
                    ImageColor.getrgb(new[key])) for key in original]
    return color_pairs


def create_map_from_json(original, new):
    color_pairs = []
    with open(original) as original_json:
        original_parsed = json.load(original_json)
    with open(new) as new_json:
        new_parsed = json.load(new_json)

    for key in original_parsed["mono"]:
        lower = original_parsed["mono"][key]["lower"]
        upper = original_parsed["mono"][key]["upper"]
        new = new_parsed["mono"][key]
        lower_rgb = hex_to_rgb(lower)
        upper_rgb = hex_to_rgb(upper)
        new_rgb = hex_to_rgb(new)

        intermediate_colors = generate_grays_between(lower_rgb, upper_rgb)
        color_pairs += [(intermediate_color, new_rgb)
                        for intermediate_color in intermediate_colors]
    return color_pairs


def hex_to_rgb(hex):
    return ImageColor.getrgb(hex)


def generate_grays_between(lower_rgb, upper_rgb):
    colors = []
    for gray in range(lower_rgb[0], upper_rgb[0] + 1):
        colors.append((gray, gray, gray))
    return colors
