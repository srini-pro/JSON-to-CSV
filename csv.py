import pyautogui as p
import os
p.alert('quick guide: enter your file address')
p.alert('starting json to csv - srinivasasan P')
renamee=p.prompt('enter your file name')
pre, ext = os.path.splitext(renamee)
os.rename(renamee, pre + '.csv')

with open(renamee, 'r+') as f:
    file_source = f.read()
    replace_string = file_source.replace('{', ' ')
    replace_string = file_source.replace('}', ' ')
    replace_string = file_source.replace('"', ' ')
    replace_string = file_source.replace(':', ',')
    replace_string = file_source.replace('":', ' ')
    replace_string = file_source.replace('}"', ' ')
    replace_string = file_source.replace('"{', ' ')

