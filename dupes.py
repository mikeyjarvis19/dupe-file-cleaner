import pathlib
import re
import fire
import shutil
import logging

regex_pattern = r".+\(\d\)"
regex = re.compile(regex_pattern)
log_location = pathlib.Path(__file__).parent.absolute() / "duplicates.log"
logging.basicConfig(filename=str(log_location),level=logging.INFO)

def bytes_to_mb(bytes):
    return bytes / 1024 / 1024

def is_dupe_filename(filename):
    result = regex.match(filename)
    return result is not None

def print_and_log(message):
    print(message)
    logging.info(message)

def can_find_original_file(dupe_path):
    """
    Searches for original filename that corresponds to the potential duplicate.

    :param dupe_path: Path of potential duplicate file.
    :type dupe_path: str
    :return: True if original file is found, else False.
    :rtype: bool
    """
    print_and_log(f'Potential duplicate: "{dupe_path}"')
    possible_original_filenames = [
        str(dupe_path)[:-8] + dupe_path.suffix,
        str(dupe_path)[:-7] + dupe_path.suffix
        ]
    for filename in possible_original_filenames:
        print_and_log(f'Looking for original file at: "{filename}"')
        if pathlib.Path(filename).exists():
            print_and_log(f'Found original file: "{filename}"')
            return True
        print_and_log(f'Original file not found: "{filename}"')
    print_and_log(f'Could not find original file for suspected duplicate: "{dupe_path}"')
    return False

def clean_dupe_files(files, starting_directory):
    dupe_dir = starting_directory / "DUPES"
    dupe_dir.mkdir(parents=True, exist_ok=True)
    for file in files:
        print_and_log(f'Moving file "{file}" to "{dupe_dir / file.name}"')
        shutil.copy(file, dupe_dir)

def look_for_dupes(starting_directory, clean_dupes=False):
    starting_path = pathlib.Path(starting_directory)
    total_filezise = 0
    duplicate_files = 0
    extensions = ["jpg", "png"]
    paths_to_clean = []
    for extension in extensions:
        for path in starting_path.rglob(f'*.{extension}'):
            if is_dupe_filename(str(path)) and can_find_original_file(path):
                print_and_log(f'Found duplicate file at: "{path}"')
                paths_to_clean.append(path)
                filesize_bytes = path.stat().st_size
                filesize_mb = bytes_to_mb(filesize_bytes)
                total_filezise += filesize_mb
                duplicate_files += 1
    if clean_dupes:
        clean_dupe_files(paths_to_clean, starting_path)

    print_and_log(f'Total duplicate files found: {duplicate_files}')
    print_and_log(f'Estimated total size of duplicate files: {round(total_filezise, 2)} MB')
    print_and_log(f'Full log saved at: "{log_location}"')

if __name__ == '__main__':
    # Example command: `python dupes.py --starting_directory "D:\Photos backup" --clean_dupes`
    fire.Fire(look_for_dupes)
