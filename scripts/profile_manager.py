import os

PROFILES_PATH = "./profiles/"
PROFILE_EXTENSION = ".profile"

def load_profile(profile_name):
    file = ""
    with os.scandir(PROFILES_PATH) as it:
        for entry in it:
            if entry.is_file() and entry.name == profile_name + PROFILE_EXTENSION:
                file = entry.path
    data = ""
    if file == "":
        print("No profile found.")
        return
    with open(file, "r") as f:
        data = f.read().split(" ")
    return data

def remove_profile(profile_name):
    os.remove(PROFILES_PATH + profile_name + PROFILE_EXTENSION)

def create_profile(profile_name, mods):
    try:
        with open(PROFILES_PATH + profile_name + PROFILE_EXTENSION, "x") as f:
            f.write(" ".join(mods))
    except FileExistsError:
        print(f"Profile name \"{profile_name}\" is already used.")
        return