from pathlib import Path
import create_map
import retexture

original_colors_hex = {
    'frame': '#c6c6c6',
    'cell': '#8b8b8b',
    'cell_border_light': '#ffffff',
    'cell_border_dark': '#373737',
    'bottom_border': '#555555',
    'border': '#000000'
    
}

final_colors_hex = {
    'frame': '#836046',
    'cell': '#75543d',
    'cell_border_light': '#a1826b',
    'cell_border_dark': '#513721',
    'bottom_border': '#664730',
    'border': '#2b190b',
}

pallete = {
  'black':'#2b190b',
  'darker_gray': '#513721',
  'dark_gray': '#664730',
  'gray': '#664730',
  'light_gray':'#836046',
  'white':'#a1826b'
}

grays_original_hex = {
  #darker gray
  'empty_background_89':'#242424',
  'empty_background_99':'#252525',
  'empty_background_00':'#262626',
  'empty_background_01':'#272727',
  'empty_background_02':'#282828',
  'empty_background_03':'#292929',
  'empty_background_04':'#2a2a2a',
  'empty_background_05':'#2b2b2b',
  'empty_background_06':'#2c2c2c',
  'empty_background_07':'#2d2d2d',
  'empty_background_08':'#2e2e2e',
  'empty_background_09':'#2f2f2f',
  'empty_background_10':'#303030',
  'empty_background_11':'#313131',
  'empty_background_12':'#323232',
  'empty_background_13':'#333333',
  'empty_background_14':'#343434',
  #dark gray
  'solid_shadow_00':'#4f4f4f',
  'solid_shadow_01':'#505050',
  'solid_shadow_02':'#515151',
  'solid_shadow_03':'#525252',
  'solid_shadow_04':'#535353',
  'solid_shadow_05':'#545454',
  'solid_shadow_06':'#555555',
  'solid_shadow_07':'#565656',
  'solid_shadow_08':'#575757',
  'solid_shadow_09':'#585858',
  'solid_shadow_10':'#595959',
  'solid_shadow_11':'#5a5a5a',
  'solid_shadow_12':'#5b5b5b',
  'solid_shadow_13':'#5c5c5c',
  'solid_shadow_14':'#5d5d5d',
  'solid_shadow_15':'#5e5e5e',
  'solid_shadow_16':'#5f5f5f',
  'solid_shadow_17':'#606060',
  #gray
  'solid_background_96':'#616161',
  'solid_background_97':'#626262',
  'solid_background_98':'#636363',
  'solid_background_99':'#646464',
  'solid_background_00':'#656565',
  'solid_background_01':'#666666',
  'solid_background_02':'#676767',
  'solid_background_03':'#686868',
  'solid_background_04':'#696969',
  'solid_background_05':'#6a6a6a',
  'solid_background_06':'#6b6b6b',
  'solid_background_07':'#6c6c6c',
  'solid_background_08':'#6d6d6d',
  'solid_background_09':'#6e6e6e',
  'solid_background_10':'#6f6f6f',
  'solid_background_11':'#707070',
  'solid_background_12':'#717171',
  'solid_background_13':'#727272',
  'solid_background_14':'#737373',
  'solid_background_15':'#747474',
  'solid_background_16':'#757575',
  'solid_background_17':'#767676',
  'solid_background_18':'#777777',
  'solid_background_19':'#787878',
  'solid_background_20':'#797979',
  'solid_background_21':'#7a7a7a',
  'solid_background_22':'#7b7b7b',
  'solid_background_23':'#7c7c7c',
  'solid_background_24':'#7d7d7d',
  'solid_background_25':'#7e7e7e',
  'solid_background_26':'#7f7f7f',
  'solid_background_27':'#808080',
  'solid_background_28':'#818181',

  #light gray
  'solid_border_light_98':'#a4a4a4',
  'solid_border_light_99':'#a5a5a5',
  'solid_border_light_00':'#a6a6a6',
  'solid_border_light_01':'#a7a7a7',
  'solid_border_light_02':'#a8a8a8',
  'solid_border_light_03':'#a9a9a9',
  'solid_border_light_04':'#aaaaaa',
  'solid_border_light_05':'#ababab',
  'solid_border_light_06':'#acacac',
  'solid_border_light_07':'#adadad',
  'solid_border_light_08':'#aeaeae',
  'solid_border_light_09':'#afafaf',
  'solid_border_light_10':'#b0b0b0',
  'solid_border_light_11':'#b1b1b1',

  #whites
  'white_00':'#d0d0d0'

}

grays_final_hex = {
  #darker gray
  'empty_background_89':pallete['darker_gray'],
  'empty_background_99':pallete['darker_gray'],
  'empty_background_00':pallete['darker_gray'],
  'empty_background_01':pallete['darker_gray'],
  'empty_background_02':pallete['darker_gray'],
  'empty_background_03':pallete['darker_gray'],
  'empty_background_04':pallete['darker_gray'],
  'empty_background_05':pallete['darker_gray'],
  'empty_background_06':pallete['darker_gray'],
  'empty_background_07':pallete['darker_gray'],
  'empty_background_08':pallete['darker_gray'],
  'empty_background_09':pallete['darker_gray'],
  'empty_background_10':pallete['darker_gray'],
  'empty_background_11':pallete['darker_gray'],
  'empty_background_12':pallete['darker_gray'],
  'empty_background_13':pallete['darker_gray'],
  'empty_background_14':pallete['darker_gray'],
  #dark gray
  'solid_shadow_00':pallete['dark_gray'],
  'solid_shadow_01':pallete['dark_gray'],
  'solid_shadow_02':pallete['dark_gray'],
  'solid_shadow_03':pallete['dark_gray'],
  'solid_shadow_04':pallete['dark_gray'],
  'solid_shadow_05':pallete['dark_gray'],
  'solid_shadow_06':pallete['dark_gray'],
  'solid_shadow_07':pallete['dark_gray'],
  'solid_shadow_08':pallete['dark_gray'],
  'solid_shadow_09':pallete['dark_gray'],
  'solid_shadow_10':pallete['dark_gray'],
  'solid_shadow_11':pallete['dark_gray'],
  'solid_shadow_12':pallete['dark_gray'],
  'solid_shadow_13':pallete['dark_gray'],
  'solid_shadow_14':pallete['dark_gray'],
  'solid_shadow_15':pallete['dark_gray'],
  'solid_shadow_16':pallete['dark_gray'],
  'solid_shadow_17':pallete['dark_gray'],
  #gray
  'solid_background_96':pallete['gray'],
  'solid_background_97':pallete['gray'],
  'solid_background_98':pallete['gray'],
  'solid_background_99':pallete['gray'],
  'solid_background_00':pallete['gray'],
  'solid_background_01':pallete['gray'],
  'solid_background_02':pallete['gray'],
  'solid_background_03':pallete['gray'],
  'solid_background_04':pallete['gray'],
  'solid_background_05':pallete['gray'],
  'solid_background_06':pallete['gray'],
  'solid_background_07':pallete['gray'],
  'solid_background_08':pallete['gray'],
  'solid_background_09':pallete['gray'],
  'solid_background_10':pallete['gray'],
  'solid_background_11':pallete['gray'],
  'solid_background_12':pallete['gray'],
  'solid_background_13':pallete['gray'],
  'solid_background_14':pallete['gray'],
  'solid_background_15':pallete['gray'],
  'solid_background_16':pallete['gray'],
  'solid_background_17':pallete['gray'],
  'solid_background_18':pallete['gray'],
  'solid_background_19':pallete['gray'],
  'solid_background_20':pallete['gray'],
  'solid_background_21':pallete['gray'],
  'solid_background_22':pallete['gray'],
  'solid_background_23':pallete['gray'],
  'solid_background_24':pallete['gray'],
  'solid_background_25':pallete['gray'],
  'solid_background_26':pallete['gray'],
  'solid_background_27':pallete['gray'],
  'solid_background_28':pallete['gray'],

  #light gray
  'solid_border_light_98':pallete['light_gray'],
  'solid_border_light_99':pallete['light_gray'],
  'solid_border_light_00':pallete['light_gray'],
  'solid_border_light_01':pallete['light_gray'],
  'solid_border_light_02':pallete['light_gray'],
  'solid_border_light_03':pallete['light_gray'],
  'solid_border_light_04':pallete['light_gray'],
  'solid_border_light_05':pallete['light_gray'],
  'solid_border_light_06':pallete['light_gray'],
  'solid_border_light_07':pallete['light_gray'],
  'solid_border_light_08':pallete['light_gray'],
  'solid_border_light_09':pallete['light_gray'],
  'solid_border_light_10':pallete['light_gray'],
  'solid_border_light_11':pallete['light_gray'],

  #whites
  'white_00':pallete['white']

}

original_all = original_colors_hex
original_all.update(grays_original_hex)

final_all = final_colors_hex
final_all.update(grays_final_hex)

colors = create_map.create_map(original_all,final_all)
folder_path = Path('../static') / '1.20.1' / 'gui'
# folder_path = Path('../static') / 'custom' / 'assets'
retexture.retexture(folder_path,colors)