#a program that walks through a folder tree and searches for files with a certain file extension then copy from whatever location they are to a new folder

import os
import shutil
#prompt the user to enter the path, extension and destination
path = input('Enter the absolute path of the directory you wish to copy from: ')

ext = input("Enter the extension you would like to copy: ")

destination = input("Enter destination folder's absolute filepath: ")
#go through all the folders and files and copy the files to the destination folder
for folders, subfolders, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith('{}'.format(ext)):
            shutil.copy(os.path.join(folders, filename), destination)

