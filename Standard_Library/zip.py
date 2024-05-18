# ----- Zip Files -----

from pathlib import Path

from zipfile import ZipFile

# Creating Zip Files
all_zip = ZipFile("13_Standard_Library/zip_files/all.zip", "w")
py_zip = ZipFile("13_Standard_Library/zip_files/py.zip", "w")

print(py_zip)
print(type(all_zip))

# Adding Files to Zip Files (zipping files)
# Approach One ---> all files
for path in Path("13_Standard_Library/social").rglob("*.*"):
    all_zip.write(path)
all_zip.close()
#! if there will be an exception or error then this for loop will not be finished
#! and this opened will won't be closed, so be careful with such cases

# Approach Two ---> py files
with ZipFile("13_Standard_Library/zip_files/py.zip", "w") as py_files:
    for path in Path("13_Standard_Library/social").rglob("*.py"):
        py_files.write(path)

#! good point about using With Statement is that, even if there will be an error,
#! it will close the opened file
# ? so better to use "With Statement" then "for loops" while working with files


# to read what is inside the zip file
with ZipFile("13_Standard_Library/zip_files/all.zip") as all_files:
    print(all_files.namelist())

# getting a single zipped file's info
with ZipFile("13_Standard_Library/zip_files/py.zip") as file_info:
    info = file_info.getinfo("13_Standard_Library/social/main.py")
    print(info.file_size)
    print(info.compress_size)
    print(info.orig_filename)
    print(info.__module__)


# extracting zip files
with ZipFile("13_Standard_Library/zip_files/all.zip") as all_files_z:
    all_files_z.extractall("13_Standard_Library/Extracted")


with ZipFile("13_Standard_Library/zip_files/py.zip") as py_unzip:
    py_unzip.extractall("13_Standard_Library/Extracted/py_files")
