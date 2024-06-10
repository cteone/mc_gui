from pathlib import Path
import create_map
import retexture

colors = create_map.create_map_override("pallete_override.json")
colors += create_map.create_map_from_json(
    "pallete_original.json", "pallete_new.json")
print(colors)
# colors = create_map.create_map(original_all,final_all)
folder_path = Path('../static') / '1.20.1' / 'gui'
# folder_path = Path('../static') / 'custom' / 'assets'
retexture.retexture(folder_path, colors)
