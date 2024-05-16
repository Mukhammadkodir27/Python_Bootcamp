# ----- Files -----

from pathlib import Path
from time import ctime
# also this module allows to convert seconds into human readable time
# ctime module is used to convert unix based date time to our date time, so that we understand our files data
# ex: creation time, modification time, and last access time

source = Path("13_Standard_Library/property_dealer/property.py")
new_source = Path("13_Standard_Library/property_dealer/app.py")
my_directory = Path("13_Standard_Library/property_dealer/__init__.py")

print(source.name)  # now source is file.py, it is a file not a path
# the last path, here app.py is new_source
print(type(new_source))

#! Useful File Methods

#! 1 - exists() ->> Checking whether or not file exists
print(source.exists())
print(new_source.exists())
print(my_directory.exists())
#! 2 - rename() ->> renaming the file
# * source.rename("13_Standard_Library/property_dealer/app.py")
#! 3 - unlink() ->> removing the file
# * new_source.unlink()
#! 4 - stat() ->> returns info about the file
print(my_directory.stat())
print(ctime(my_directory.stat().st_atime))  # last access time
print(ctime(my_directory.stat().st_mtime))  # last modification time
print(ctime(my_directory.stat().st_ctime))  # creation time

# ? The following 4 methods take care of opening and closing the file ...
#! 5 - read_bytes() ->> reading data from a file and returns the content of the file as a bytes object for representing binary data

#! 6 - read_text() ->> reading the content of the file as a string

#! 7 - write_bytes() ->> writing to a file

#! 8 - write_text() ->> writing to a file as a string

#! 9 - Copying a file to another location
