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

def look_for_dupes(starting_directory):
    starting_path = pathlib.Path(starting_directory)
    total_filezise = 0
    extensions = ["jpg", "png"]
    paths_to_clean = []
    for extension in extensions:
        for path in starting_path.rglob(f'*.{extension}'):
            if is_dupe_filename(str(path)):
                filesize_bytes = path.stat().st_size
                filesize_mb = bytes_to_mb(filesize_bytes)
                total_filezise += filesize_mb
                paths_to_clean.append(path)
                print(path)
    
    print(f"Total filesize: {total_filezise}MB")

if __name__ == '__main__':
    # Example command: `python dupes.py --starting_directory "E:\Pictures"`
  fire.Fire(look_for_dupes)
