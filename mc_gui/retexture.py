from pathlib import Path
import process_image
import json

# def recursively_iterate_folder(path):
#   folder_path = Path(path)
#   for entry in folder_path.iterdir():
#     if entry.is_file():
#       print("file:", entry)
#     elif entry.is_dir():
#       recursively_iterate_folder(entry)



# recursively_iterate_folder(folder_path)

# folder_path = Path('../static') / '1.20.6' / 'gui'

def unpack_ignore(ignore):
  with open(ignore) as ignore_json:
    ignore_parsed = json.load(ignore_json)
    print(ignore_parsed)
  return ignore_parsed


def retexture(path,colors):
  ignore_dict = unpack_ignore("ignore.json")
  folder_path = Path(path)
  for entry in folder_path.iterdir():
    if entry.is_file():
      if not entry.name in ignore_dict['files']:
        if entry.suffix == '.png':
          (ellipses,static, *rest) = entry.parts
          output = Path('../output',*rest)
          process_image.change_colors_tolerance(entry,output,colors,5)
          print("retextured:", output)
    elif entry.is_dir():
      if not entry.name in ignore_dict['directories']:
        retexture(entry,colors)

