from pathlib import Path
import process_image

# def recursively_iterate_folder(path):
#   folder_path = Path(path)
#   for entry in folder_path.iterdir():
#     if entry.is_file():
#       print("file:", entry)
#     elif entry.is_dir():
#       recursively_iterate_folder(entry)



# recursively_iterate_folder(folder_path)

# folder_path = Path('../static') / '1.20.6' / 'gui'

def retexture(path,colors):
  folder_path = Path(path)
  for entry in folder_path.iterdir():
    if entry.is_file():
      if entry.suffix == '.png':
        (ellipses,static, *rest) = entry.parts
        output = Path('../output',*rest)
        process_image.change_colors_tolerance(entry,output,colors,3)
        print("file:", output)
    elif entry.is_dir():
      retexture(entry,colors)

