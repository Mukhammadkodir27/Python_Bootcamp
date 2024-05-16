# Directories

from pathlib import Path

my_directory = Path("real_estate")
new_directory = Path("social")
# * date_time = Path("14_Date")
this_directory = Path("13_Standard_Library")

#! ------- Useful Directory Methods -------

# !1 - exists() ->> to check whehter or not the directory exists
# * print(my_directory.exists())
# * print(new_directory.exists())
#! 2 - mkdir() ->> to create new directory
# * my_directory.mkdir()
# * new_directory.mkdir()
#! 3 - rmdir() ->> to remove the existing directory
# * my_directory.rmdir()
# * new_directory.rmdir()
#! 4 - rename() ->> renaming the directory
# * date_time.rename("14_Date_and_Time")
#! 5 - iterdir() ->> getting the list of files and directories at this path
# will get generator object not the files inside this dir
print(this_directory.iterdir())
# to solve this we need to use for loop
for files in this_directory.iterdir():
    print(files)
# List Comprehension
existing_data = [data for data in this_directory.iterdir()]
print(existing_data)
#! 6 - is_file() ->> getting only the files
only_files = [files for files in this_directory.iterdir() if files.is_file()]
print(only_files)
#! 7 - is_dir() ->> getting only the directories
only_folders = [folders for folders in this_directory.iterdir()
                if folders.is_dir()]
print(only_folders)
#! Case 1: Searching using a pattern using the asterisk (*) symbol
directories = [data for data in this_directory.iterdir() if data.is_dir()]
# it takes only the files which end with .py, as given *.py
python_files = [files for files in this_directory.glob("*.py")]
html_files = [files for files in this_directory.glob("*.html")]  # html files
any_files = [files for files in this_directory.glob("*.*")]  # any files

files = [python_files, html_files, any_files]
for file in files:
    print("filename: ", file)

#! Case 2: Searching recursively using the rglob() method
all_existing_files = [data for data in this_directory.rglob("*.*")]
print(all_existing_files)

all_files = [data for data in Path("10_OOP").rglob("*.*")]
print(all_files)

many_files = [data for data in Path().iterdir() if data.is_dir()
              or data.is_file()]

print(many_files)

