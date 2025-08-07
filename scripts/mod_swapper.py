import os
import shutil

def get_directories(from_path:str, ignore: list[str] = None, must_load: list[str] = None) -> list[str]:
    if not ignore:
        ignore = []
    result = []
    with os.scandir(from_path) as it:
        for entry in it:
            if entry.is_dir() and entry.name not in ignore and not must_load:
                result.append(entry.path)
            elif entry.is_dir() and must_load and entry.name in must_load and entry.name not in ignore:
                result.append(entry.path)
    return result

def get_simple_dirs(from_path:str, ignore: list[str] = None) -> list:
    if not ignore:
        ignore = []
    result = []
    with os.scandir(from_path) as it:
        for entry in it:
            if entry.is_dir() and entry.name not in ignore:
                result.append(entry.name)
    return result

def insert_into_pool(from_path:str, pool_path: str) -> None:
    dirs = get_directories(from_path, ["lovely"])
    pool_dirs = []
    with os.scandir(pool_path) as it:
        for entry in it:
            if entry.is_dir():
                pool_dirs.append(entry.path)
    for directory in dirs:
        if directory not in pool_dirs:
            shutil.move(directory, pool_path)
        else:
            print(f"Cannot safely move {directory} into pool: duplicate found")

def insert_from_pool(pool_path:str, insert_into: str, dirs:list = None):
    if not dirs:
        dirs = get_directories(pool_path, ["lovely"])
    dest_dirs = []
    with os.scandir(insert_into) as it:
        for entry in it:
            if entry.is_dir():
                dest_dirs.append(entry.path)
    for directory in dirs:
        if directory not in dest_dirs:
            try:
                shutil.move(directory, insert_into)
            except FileNotFoundError:
                print(f"{directory} not found.")
        else:
            print(f"Cannot safely move {directory} from pool: duplicate found")

if __name__ == "__main__":
    insert_into_pool("C:\\users\\user\\appdata\\roaming\\balatro\\mods", "./mod_pool")

    input()

    # insert_from_pool("./mod_pool", "C:\\users\\user\\appdata\\roaming\\balatro\\mods")