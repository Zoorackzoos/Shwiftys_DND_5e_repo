"""
the other file of this name:
"actions_only_input_file.md"
is used if you want to update a creature using the markdown file interpolation system,
and the spreadsheet update system.

this file:
"actions_only_input_file.py"
is used if you want to instead update a creature using the spreadsheet update system.
it's different because instead of making the interpreter help you, you are making the python file
the interrupter creates.

to keep directory consistency, to update the monster in the spreadsheet you have to go to
"update_actions_only_python_file_and_update_based_on_name.py"

the values between "name" and "actions" are:
    * core spreadsheet values
        * size
        * type
        * CR
        * URL
        * font
        * author
        * HP
        * AC
        * speed
        * align
        * str
        * dex
        * con
        * int
        * wis
        * cha
        * saving throws
        * skills
        * WEAKNESSES_RESISTANCES_AND_IMMUNITIES
        * senses
        * languages
        * additional
    * CR crafter - additional values
        * average damage
        * attack modifier
        * has legendary action
        * legendary action damage
        * has flight
        * resistance count
        * immunity count
        * resistance count
        * save dc
        * is spellcaster
        * regeneration per round
        * multiattack count
        * ability count
        * ability cr weight
        * recharge damage
        * limited use damage
        * bonus action damage

    this uses enums in:
    * spreadsheet_enums.py
    * markdown_interpreter_related_enums.py
"""
from universal_functions.enums import spreadsheet_enums, markdown_interpreter_related_enums

actions_only_input_file_monster_dict = \
    {
        spreadsheet_enums.SpreadsheetKeysEnums.NAME.value :
            'Misc. Creature, Giant Rat',
        spreadsheet_enums.SpreadsheetKeysEnums.ACTIONS.value :
            [
                #------------------------ TRAITS START -----------------------
                {
                    markdown_interpreter_related_enums.ActionKeyEnums.NAME.value:
                        "Keen Smell",
                    markdown_interpreter_related_enums.ActionKeyEnums.NOTES.value:
                        "The rat has advantage on Wisdom (Perception) checks that rely on smell."
                },
                {
                    markdown_interpreter_related_enums.ActionKeyEnums.NAME.value:
                        "Pack Tactics",
                    markdown_interpreter_related_enums.ActionKeyEnums.NOTES.value:
                        "The rat has advantage on an attack roll against a creature if at least one of the rat's allies is within 5 ft. of the creature and the ally isn't incapacitated."
                },
                # ------------------------ TRAITS END -----------------------
                # ----------------------- ATTACK START ----------------
                {
                    markdown_interpreter_related_enums.ActionKeyEnums.NAME.value:
                        "Bite",
                    markdown_interpreter_related_enums.ActionKeyEnums.ACTION_TYPE.value:
                        markdown_interpreter_related_enums.ActionTypeEnums.ACTION.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value:
                        markdown_interpreter_related_enums.AttackTypeEnums.MELEE_ATTACK.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.HIT_MODIFIER.value:
                        4,
                    markdown_interpreter_related_enums.ActionKeyEnums.RANGE.value:
                        5,
                    markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE.value:
                        "1d4 + 2",
                    markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE_TYPE.value:
                        markdown_interpreter_related_enums.DamageTypeEnums.PIERCING.value,
                },
                # ----------------------- ATTACK END ----------------

                #keep this around and comment it out or in because you'll see this alot
                """
                {
                    markdown_interpreter_related_enums.ActionKeyEnums.NAME.value:
                        "Multiattack",
                    markdown_interpreter_related_enums.ActionKeyEnums.ACTION_TYPE.value:
                        markdown_interpreter_related_enums.ActionTypeEnums.PASSIVE.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value:
                        markdown_interpreter_related_enums.AttackTypeEnums.UTILITY.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.NOTES.value:
                        "The devil makes two attacks with its chains."
                }
                """
            ],
    }
