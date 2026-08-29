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
"""
from universal_functions.vars.enums import spreadsheet_enums, markdown_interpeter_related_enums

actions_only_input_file_monster_dict = \
    {
        spreadsheet_enums.SpreadsheetKeysEnums.NAME.value :
            'Goblin',
        "actions" :
            [
                {
                    "name": "scimitar",
                    "action_type": markdown_interpeter_related_enums.ActionTypeEnums.ACTION.value,
                    "attack_type": markdown_interpeter_related_enums.AttackTypeEnums.MELEE_ATTACK.value,
                    "hit_modifier": 4,
                },
                {
                    'name': 'action \\- test spark',
                    'action_type': 'action',
                    'attack_type': 'ranged_spell_attack',
                    'hit_modifier': 4,
                    'damage': '1d6 + 2',
                    'damage_type': 'fire',
                    'range': 60,
                    'notes': 'Link in the action name should become plain text.'
                 },
                {
                    'name': 'action \\- bad math shove',
                    'action_type': 'bonus_action',
                    'attack_type': 'saving_throw',
                    'save_dc': 11,
                    'save_stat': 'str',
                    'damage': '1d4 \\- 1',
                    'damage_type': 'bludgeoning',
                    'range': 5,
                    'notes': 'Negative constants should not scare the parser.'
                 }
            ],
    }
