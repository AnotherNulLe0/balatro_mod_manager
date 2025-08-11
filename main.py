import scripts.mod_swapper as mod_swapper
import scripts.profile_manager as profile_manager
import sys
import os

balatro_mod_dir = ""
mod_pool_dir = "./mod_pool"
clear_command = ""

if sys.platform == "win32":
    balatro_mod_dir = os.getenv("appdata")+"\\Balatro\\Mods"
    clear_command = "cls"
else:
    raise NotImplementedError("Not implemented for non-Windows platforms")

promt = "1 - load profile\n2 - create profile\n3 - delete profile\n4 - unload all\n"
while action := input(promt):
    match action:
        case "1":
            profile_name = input("Profile name: ")
            if not profile_name:
                os.system(clear_command)
                continue
            mod_list = profile_manager.load_profile(profile_name)
            if mod_list:
                mod_list = list(map(lambda x: f"{mod_pool_dir}/{x}", mod_list))
                mod_swapper.insert_into_pool(balatro_mod_dir, mod_pool_dir)
                mod_swapper.insert_from_pool(mod_pool_dir, balatro_mod_dir, mod_list)
                print(f"Successfully loaded profile \"{profile_name}\"")
        case "2":
            profile_name = input("Profile name: ")
            if not profile_name:
                os.system(clear_command)
                continue
            choice = input("Do you want to create a profile with currently installed mods, or with only selected ones?\n1 - currently installed\n2 - mods of your choice\n")
            mod_list = None
            match choice:
                case "1":
                    mod_list = mod_swapper.get_simple_dirs(balatro_mod_dir, ["lovely"])
                case "2":
                    mod_list = input("Please enter your mod names separated by space (\" \")\n").split(" ")
            if not mod_list:
                os.system(clear_command)
                continue
            profile_manager.create_profile(profile_name, mod_list)
        case "3":
            profile_name = input("Profile name: ")
            if not profile_name:
                os.system(clear_command)
                continue
            profile_manager.remove_profile(profile_name)
        case "4":
            mod_swapper.insert_from_pool(
                mod_pool_dir, 
                balatro_mod_dir, 
                None
            )
        case _:
            print()
    input("Please press enter to continue")
    os.system(clear_command)