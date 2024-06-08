from PIL import ImageColor

def create_map(original,final):
  color_pairs = [(ImageColor.getrgb(original[key]),ImageColor.getrgb(final[key])) for key in original]
  return color_pairs
