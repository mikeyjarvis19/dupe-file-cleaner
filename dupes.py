import pathlib
import re
import fire

regex_pattern = r".+\(\d\)"
regex = re.compile(regex_pattern)

def bytes_to_mb(bytes):
    return bytes * 0.000001

def is_dupe_filename(filename):
    result = regex.match(filename)
    return result is not None

def can_find_original_file(dupe_path):
    print(f"Potential duplicate: {dupe_path}")
    original_filename = dupe_path._str[:-8] + dupe_path.suffix
    print(f"Looking for original file at: {original_filename}")
    if pathlib.Path(original_filename).exists():
        print(f"Found original file: {original_filename}")
        return True
    else:
        original_filename = dupe_path._str[:-7] + dupe_path.suffix
        print(f"Looking for original file at: {original_filename}")
        if pathlib.Path(original_filename).exists():
            print(f"Found original file: {original_filename}")
            return True
        print(f"ORIGINAL FILE NOT FOUND: {original_filename}")
        return False

def look_for_dupes(starting_directory):
    starting_path = pathlib.Path(starting_directory)
    total_filezise = 0
    extensions = ["jpg", "png"]
    paths_to_clean = []
    for extension in extensions:
        for path in starting_path.rglob(f'*.{extension}'):
            if is_dupe_filename(str(path)) and can_find_original_file(path):
                print(f"Found duplicate file at: {path}")
                paths_to_clean.append(path)
                filesize_bytes = path.stat().st_size
                filesize_mb = bytes_to_mb(filesize_bytes)
                total_filezise += filesize_mb

    print(f"Total size of duplicate files: {round(total_filezise, 2)} MB")

if __name__ == '__main__':
    # Example command: `python dupes.py --starting_directory "E:\Pictures"`
  fire.Fire(look_for_dupes)
