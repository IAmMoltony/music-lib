#!/usr/bin/python3

import os
import argparse
import pathlib

def fix_wd():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

if __name__ == "__main__":
    fix_wd()

    parser = argparse.ArgumentParser(description="Delete music from music-lib")
    parser.add_argument("--dry", action="store_true", help="Don't make any actual changes")
    args = parser.parse_args()

    dry_run = args.dry

    if dry_run:
        print("Dry run mode enabled. No changes will be made.")

    ids = []
    with open("./music/archive.txt", "r") as archive:
        archive_data = archive.read()
        ids = archive_data.split("\n")
    ids = [id.removeprefix("youtube ") for id in ids] # Remove the "youtube " (note the space) prefix from IDs
    ids = list(filter(None, ids)) # Remove any empty strings from IDs

    music_files = []
    music_dir = pathlib.Path("./music")
    for id in ids:
        pattern = f"*{id}*"
        file = ""
        for file in music_dir.glob(pattern):
            file = f"./music/{file.name}"
            break
        if not file:
            print(f"(No music file found for id {id})")
            continue
        music_files.append(file)

    print(f"Found music files: {music_files}")

    print("Deleting files")
    for file in music_files:
        print(f"Deleting: {file}")
        if not dry_run:
            os.remove(file)
    print("Deleting archive")
    if not dry_run:
        os.remove("./music/archive.txt")
