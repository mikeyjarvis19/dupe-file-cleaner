import pathlib
import re

starting_directory = ""
starting_path = pathlib.Path(starting_directory)
files_found = []
paths_to_clean = []
regex_pattern = r".+\(\d\)"
regex = re.compile(regex_pattern)

def bytes_to_mb(bytes):
    return bytes * 0.000001

def is_dupe_filename(filename):
    result = regex.match(filename)
    return result is not None

extensions = ["jpg", "png"]
for extension in extensions:
    for path in starting_path.rglob(f'*.{extension}'):
        files_found.append(path)

total_filezise = 0
for path in files_found:
    if is_dupe_filename(str(path)):
        filesize_bytes = path.stat().st_size
        filesize_mb = bytes_to_mb(filesize_bytes)
        total_filezise += filesize_mb
        paths_to_clean.append(path)
        print(path)

print(f"Total filesize: {total_filezise}MB")