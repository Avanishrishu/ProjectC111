import os
import shutil

from_dir = "C:/Users/Rajnish prabhakar/Downloads"
to_dir = "C:/Users/Rajnish prabhakar/Desktop/Downloaded_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:
    root,ext = os.path.splitext(file)
    print(root)
