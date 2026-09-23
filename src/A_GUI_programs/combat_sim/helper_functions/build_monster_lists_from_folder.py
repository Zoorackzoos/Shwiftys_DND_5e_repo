import os
import importlib.util


def build_monster_lists_from_folder(folder_path, spreadsheet_monsters_dict_in_question):
    """
    Scans folder_path for .py files, dynamically imports each one, and calls
    its get_monster_list(spreadsheet_monsters_dict_in_question) function.

    Returns a list in the same shape you're already using:
        [ [display_name, monster_list], [display_name, monster_list], ... ]

    Bad paths, malformed files, or files missing get_monster_list are skipped
    with a printed warning rather than crashing the whole program.

    claude made this 🥀🥀🥀
    """
    results = []

    # --- validate the folder path itself first ---
    if not os.path.exists(folder_path):
        print(f"ERROR: build_monster_lists_from_folder: path does not exist: {folder_path}")
        return results

    if not os.path.isdir(folder_path):
        print(f"ERROR: build_monster_lists_from_folder: path is not a directory: {folder_path}")
        return results

    for filename in os.listdir(folder_path):
        if not filename.endswith(".py"):
            continue
        if filename == "__init__.py":
            continue

        full_path = os.path.join(folder_path, filename)
        module_name = filename[:-3]  # strip ".py" for a clean module name

        try:
            spec = importlib.util.spec_from_file_location(module_name, full_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        except Exception as e:
            print(f"ERROR: build_monster_lists_from_folder: failed to import {filename}: {e}")
            continue

        if not hasattr(module, "get_monster_list"):
            print(f"ERROR: build_monster_lists_from_folder: {filename} has no get_monster_list() function, skipping.")
            continue

        try:
            monster_list = module.get_monster_list(
                spreadsheet_monsters_dict_in_question=spreadsheet_monsters_dict_in_question
            )
        except Exception as e:
            print(f"ERROR: build_monster_lists_from_folder: {filename}'s get_monster_list() raised an error: {e}")
            continue

        display_name = module_name  # or derive a nicer label from the file if you prefer
        results.append([display_name, monster_list])

    return results