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
            'Dragon, Chromatic, Black, Young',
        spreadsheet_enums.SpreadsheetKeysEnums.ACTIONS.value :
            [
                #------------------------ TRAITS START -----------------------
                {
                    markdown_interpreter_related_enums.ActionKeyEnums.NAME.value:
                        "Amphibious",
                    markdown_interpreter_related_enums.ActionKeyEnums.NOTES.value:
                        "The dragon can breathe air and water."
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
                        7,
                    markdown_interpreter_related_enums.ActionKeyEnums.RANGE.value:
                        10,
                    markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE.value:
                        "2d10 + 1d8 + 4",
                    markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE_TYPE.value:
                        markdown_interpreter_related_enums.DamageTypeEnums.PIERCING.value,
                },
                {
                    markdown_interpreter_related_enums.ActionKeyEnums.NAME.value:
                        "Claw",
                    markdown_interpreter_related_enums.ActionKeyEnums.ACTION_TYPE.value:
                        markdown_interpreter_related_enums.ActionTypeEnums.ACTION.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value:
                        markdown_interpreter_related_enums.AttackTypeEnums.MELEE_ATTACK.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.HIT_MODIFIER.value:
                        7,
                    markdown_interpreter_related_enums.ActionKeyEnums.RANGE.value:
                        5,
                    markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE.value:
                        "2d6 + 4",
                    markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE_TYPE.value:
                        markdown_interpreter_related_enums.DamageTypeEnums.SLASHING.value,
                },
                {
                    markdown_interpreter_related_enums.ActionKeyEnums.NAME.value:
                        "Acid Breath",
                    markdown_interpreter_related_enums.ActionKeyEnums.ACTION_TYPE.value:
                        markdown_interpreter_related_enums.ActionTypeEnums.RECHARGEABLE_ACTION.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value:
                        markdown_interpreter_related_enums.AttackTypeEnums.SAVING_THROW.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.SAVE_STAT.value:
                        spreadsheet_enums.SavingThrowsEnums.DEX.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.SAVE_DC.value:
                        14,
                    markdown_interpreter_related_enums.ActionKeyEnums.RANGE.value:
                        30,
                    markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE.value:
                        "11d8",
                    markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE_TYPE.value:
                        markdown_interpreter_related_enums.DamageTypeEnums.ACID.value,
                },
                # ----------------------- ATTACK END ----------------

                # ----------------------- MULTI ATTACK START --------------------------

                {
                    markdown_interpreter_related_enums.ActionKeyEnums.NAME.value:
                        "Multiattack",
                    markdown_interpreter_related_enums.ActionKeyEnums.ACTION_TYPE.value:
                        markdown_interpreter_related_enums.ActionTypeEnums.PASSIVE.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value:
                        markdown_interpreter_related_enums.AttackTypeEnums.UTILITY.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.NOTES.value:
                        "The dragon makes three attacks: one with its bite and two with its claws."
                }

                # ----------------------- MULTI ATTACK END --------------------------
            ],
    }
