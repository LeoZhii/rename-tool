# rename.py must be in the same directory as all other files
# don't include file type eg. ".pdf"
# on windows: "run as administrator"
# on mac: run in terminal and allow access OR sudo python3 rename.py

import os
import shutil

option = int(input(
    "Choose an Option:\n1. To rename the entire name.\n2. To add to the beginning.\n3. To add to the end.\n"))

print("What you like to rename/add? Use $ to replace incrementing integers.")

rename = input().replace("\n", "")
int = 1

if os.path.exists("renamed_files"):
    shutil.rmtree("renamed_files")

os.mkdir("renamed_files")

for old_filename in os.listdir('.'):
    if old_filename == 'rename.py' or old_filename == "renamed_files" or old_filename.startswith("."):
        continue
    temp = old_filename.split(".")

    if option == 1:
        new_filename = (rename+"."+temp[1]).replace("$", str(int))

    elif option == 2:
        new_filename = (rename+temp[0]+"."+temp[1]).replace("$", str(int))

    elif option == 3:
        new_filename = (temp[0]+rename+"."+temp[1]).replace("$", str(int))

    shutil.copy(old_filename, os.path.join("renamed_files", old_filename))
    shutil.move(os.path.join("renamed_files", old_filename),
                os.path.join("renamed_files", new_filename))

    int += 1
print("success\n")
