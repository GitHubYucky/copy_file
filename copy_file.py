from tkinter import filedialog
from tkinter import *
from shutil import copy2
import os

root = Tk()
root.withdraw()

source = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("XLSX Files","*.xlsx"), ("all files", "*.*")))
source = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("XLSX Files","*.xlsx"), ("all files", "*.*")))

# target = 'import'
dir_parts = list(os.path.split(source))
file_name=dir_parts[1]
# print(file_name)
# target_dir = dir_parts[0] + '/' + target + '/' + dir_parts[1]
# print(target_dir)


root = Tk()
root.withdraw()
target_dir = filedialog.askdirectory()
target_dir=target_dir + '/'
# print(target_dir)

copy2(source, target_dir)
