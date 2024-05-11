# Paths

# https://docs.python.org/3/library/

from pathlib import Path

#! creating an absolute path on windows
path = Path("C:\\Program Files\\Python 3")  # "C:\Program Files\Python 3"
print(path)

#! using raw string to simplify the path creation
path = Path(r"C:\Program Files\Python 3")
print(path)

#! relative paths
path = Path("users/__init__.py")
print(path)

#! the Path() object that represents the current folder
path = Path()  # represents the current folder
print(path)

#! combining Path() objects together
path_combined = Path("available_path") / Path("additional_path")
print(path)

#! combining the Path() object with a string
path_combined_w_string = Path("any_file") / "ecommerce" / "__init__.py"
print(path_combined_w_string)

#! Getting the home directory of the current user
print(Path.home())

# ? *-*-*-*-*-*   *-*-*-*-*-*   *-*-*-*-*-*
path = Path("social/audio")
path2 = Path("social/images/__init__.py")
path3 = Path("users")

#! exists() method to check if this file or directory exists or not
# False because they are just paths not actual existing files, if they do exist then ok
print(path.exists())
print(path2.exists())  # False
print(path3.exists())  # False

#! to check if this path is a file
print(path.is_file())  # not file as it is not ending with an extension
# is a file as it has .py extension, if it existed for not it is just a path
print(path2.is_file())
print(path3.is_file())  # not file as it is not ending with an extension

#! to check if this path is a directory
print(path.is_dir())  # is a directory if existed as it does not have an extension
print(path2.is_dir())  # the last file has extension so not directory
print(path3.is_dir())  # if existed, yes directory

#! returns the file name in path (extracting individual components in this path)
print(path.name)
print(path2.name)
print(path3.name)

#! returns the file name in path without the extension
print(path.stem)
print(path2.stem)
print(path3.stem)

#! returns the file name extension
print(path.suffix)
print(path2.suffix)
print(path3.suffix)

#! returns the parent of the file
print(path.parent)  # the first file from path is paret
print(path2.parent)
# for path("users") the . will be the parent, as there is no another file before this file
print(path3.parent)

#! creates a new path with the file name changed
# here init.py from path2 is changed to initial.txt in new path3
path3 = path2.with_name("__initial__.txt")
print(path3)

#! getting the absolute path for the newly created file
print(path3.absolute())

#! changing the extension of a file
print(path3.with_suffix(".js"))
