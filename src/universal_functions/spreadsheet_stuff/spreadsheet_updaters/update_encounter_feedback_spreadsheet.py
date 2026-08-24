import csv
from pathlib import Path
from helper_functions.get_value_and_get_normalized_name_from_monster_or_encounter_dict import get_normalized_encounter_or_monster_name,get_value_from_encounter_or_monster_dict

PROJECT_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_ENCOUNTER_FEEDBACK_SPREADSHEET = (
    PROJECT_ROOT / "sheets" / "encounter_feedback.csv"
)


HEADER_ALIASES = {
    "encounter_name": ["name", "encounter"],
    "party_level": ["level"],
    "party_size": ["player_count", "players"],
    "predicted_difficulty": ["predicted"],
    "actual_difficulty": ["actual"],
    "monster_count": ["monsters"],
    "total_monster_xp": ["total_xp"],
    "adjusted_xp": ["adjusted_monster_xp"],
    "rounds": ["round_count"],
    "lasted_too_long": ["too_long"],
    "players_downed": ["downed"],
    "players_killed": ["killed", "deaths"],
    "major_resource_drain": ["resource_drain"],
    "terrain_helped_players": ["player_terrain_help"],
    "terrain_helped_monsters": ["monster_terrain_help"],
    "player_synergy_tags": ["synergy_tags"],
    "monster_weakness_tags": ["weakness_tags"],
    "party_thresholds": ["thresholds"],
}

def get_row_from_encounter_dict(encounter_dict, fieldnames):
    row = {}

    for fieldname in fieldnames:
        row[fieldname] = get_value_from_encounter_or_monster_dict(
            encounter_or_monster_dict=encounter_dict,
            header=fieldname,
            HEADER_ALIASES=HEADER_ALIASES
        )

    return row


def get_duplicate_index(rows, encounter_name):
    normalized_encounter_name = get_normalized_encounter_or_monster_name(
        encounter_or_monster_name=encounter_name
    )

    for index, row in enumerate(rows):
        if  (get_normalized_encounter_or_monster_name(
                encounter_or_monster_name=row.get("encounter_name", "")
            )
                ==
                normalized_encounter_name):
            return index

    return None


def update_encounter_feedback_spreadsheet(
        encounter_dict,
        path_to_encounter_feedback_csv_file=DEFAULT_ENCOUNTER_FEEDBACK_SPREADSHEET,
        duplicate_action="ask",
        tab_amount="\t"
):
    """
    updates the encounter_feedback.csv file.
    if you want to update the encoutner_feedback.tsv file you have to run:
    "convert_csv_file_into_tsv_file.py"

    this function and it's helper functions was coded by Codex. I modified it minorly.

    :param encounter_dict:
        lower level than my markdown and python files. only the system views these variables created by get_encounter_difficulty_from_cr_values
    :param path_to_encounter_feedback_csv_file:
        this is variable depending on the location of the dungeon file. The reason this exists is because
        i don't want to deal with more powerful path based libraries. So it just gets fed as a parameter.
    :param duplicate_action:
        it's not advized you mess with this.
    :param tab_amount: Variations of "\t". like "\t\t" or "\t\t\t".
    :return:
    """
    print(tab_amount, "update_encounter_feedback_spreadsheet")
    tab_amount += "\t"

    #Codex used the Path class because it's less archaic than just having plain strings like i do in
    #the rest of this program.
    path_to_encounter_feedback_csv_file = Path(path_to_encounter_feedback_csv_file)
    print(tab_amount, "path_to_encounter_feedback_csv_file =", path_to_encounter_feedback_csv_file)

    if not path_to_encounter_feedback_csv_file.exists():
        exit("ERROR: update_encounter_feedback_spreadsheet: encounter feedback spreadsheet does not exist.")

    #this function was a duplicate from the other updater
    # so i refactored it to use less space in the repo
    encounter_name = get_value_from_encounter_or_monster_dict(
        encounter_or_monster_dict=encounter_dict,
        header="encounter_name",
        HEADER_ALIASES=HEADER_ALIASES
    )

    if str(encounter_name).strip() == "":
        print(tab_amount, "ERROR: update_encounter_feedback_spreadsheet: encounter_dict must include an encounter_name or name value.")
        exit()

    with open(path_to_encounter_feedback_csv_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        rows = list(reader)

    if fieldnames is None:
        print(tab_amount, "ERROR: update_encounter_feedback_spreadsheet: spreadsheet must have a header row.")
        exit()

    new_row = get_row_from_encounter_dict(
        encounter_dict=encounter_dict,
        fieldnames=fieldnames
    )

    duplicate_index = get_duplicate_index(
        rows=rows,
        encounter_name=encounter_name
    )

    if duplicate_index is not None:
        print(tab_amount, "duplicate encounter found =", encounter_name)

        if duplicate_action == "ask":
            answer = input(
                "An encounter named "
                + str(encounter_name)
                + " already exists. Overwrite it? or stop the program? y/n/s: "
            )

            if answer.strip().lower() in ["y", "yes"]:
                duplicate_action = "overwrite"
            elif answer.strip().lower() in ["n", "no"]:
                duplicate_action = "continue"
            else: #answer.strip().lower() in ["s", "stop"]:
                duplicate_action = "stop"

        if duplicate_action == "overwrite":
            print(tab_amount, "overwriting existing encounter row")
            rows[duplicate_index] = new_row
        elif duplicate_action == "continue":
            print(tab_amount, "continuing encounter update...")
        elif duplicate_action == "stop":
            print(tab_amount, "stopping without changing the spreadsheet")
            exit()
        else:
            print(tab_amount, "ERROR: duplicate_action must be ask, overwrite, continue, or stop.")
            exit()
    else:
        print(tab_amount, "adding new encounter =", encounter_name)
        rows.append(new_row)

    with open(path_to_encounter_feedback_csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(tab_amount, "spreadsheet updated")
    return new_row


if __name__ == "__main__":
    example_encounter = {
        "encounter_name": "example_encounter",
        "party_level": 4,
        "party_size": 4,
        "predicted_difficulty": "medium",
        "actual_difficulty": "easy",
        "notes": "Example row.",
    }

    update_encounter_feedback_spreadsheet(
        encounter_dict=example_encounter
    )
