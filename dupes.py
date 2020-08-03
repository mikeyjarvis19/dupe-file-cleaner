import pathlib
import os


starting_directory = "C:\\Users\Mike\Desktop\\testfolder"
starting_directory = pathlib.Path(starting_directory)
paths_to_clean = []
files = []

def search_dir(item):
    if item.is_dir():
        print(f"Found new dir: {item}")
        paths_to_clean.append(item)
    if item.is_file():
        print(f"Found new file: {item}")
        files.append(item)

def check_item(item):
    if item not in paths_to_clean and item not in files:
        search_dir(item)

things = starting_directory.iterdir()
for thing in things:
    check_item(thing)

for item in paths_to_clean:
    for thing in things:
        check_item(thing)
    if item.is_dir() and item != starting_directory and item not in paths_to_clean:
        print(f"Found new dir: {item}")
        paths_to_clean.append(item)
    if item.is_file():
        files.append(item)

print("test")
