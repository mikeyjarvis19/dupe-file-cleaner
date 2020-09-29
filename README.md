# dupe-file-cleaner

This is a simple Python script that looks for files that are duplicates, and moves them into a folder where they can be deleted if desired. The script is looking specifically for `.jpg.` and `.png` files, but could be modified to look for other file types by altering `extensions` in the `look_for_dupes` function.

**WARNING: If you're not familiar with running scripts to deal with files and/or you have no idea how this script works, don't use it! I will not be responsible for you messing up your files...**

The script will search for files matching the regex pattern `.+\(\d\)`. Some example filenames that would be picked up:
* `beach_photo(1).jpg`
* `beach_photo (1).png`

Once the script has identified a potential duplicate, it will try to find the original file e.g. `beach_photo.jpg` or `beach_photo.png`. The script will only move the potential duplicate if the original file can also be found.

Duplicate files will be moved to a folder `DUPES` which will be created in the top level of the supplied starting directory.

A full log file will be created at `dupe-file-cleaner\duplicates.log`, you might want to manually clear this log out between runs of the script.

Example use of the script:
```
python dupes.py --starting_directory "D:\Photos backup" --clean_dupes
```

* `--starting_directory ` - This is the folder that will be searched for duplicates. Searching is recursive, so if you have e.g. `folder1/folder2/photo(1).png` then the duplicates will still be found.
* `--clean_dupes` - This tells the script to actually perform the cleanup and move the identified duplicates. If you run the script without this flag, it will just log/print which duplicates it would move if you DID add the flag. I recommend you run the script WITHOUT this flag at least once just to check what it's going to do looks sensible.