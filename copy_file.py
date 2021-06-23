def copy_file():
  # from tkinter import *
  from tkinter import filedialog
  from tkinter import Tk
  from shutil import copy2
  import os

  root = Tk()
  root.withdraw()

  source = filedialog.askopenfilename(initialdir="/", title="Select file")

  dir_parts = list(os.path.split(source))
  file_name=dir_parts[1]

  target_dir = filedialog.askdirectory()
  target_dir=target_dir + '/'

  copy2(source, target_dir)

copy_file()
