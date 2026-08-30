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
            'Troll, Greatmaw',
        spreadsheet_enums.SpreadsheetKeysEnums.ACTIONS.value :
            [
                {
                    markdown_interpreter_related_enums.ActionKeyEnums.NAME.value:
                        "Bite",
                    markdown_interpreter_related_enums.ActionKeyEnums.ACTION_TYPE.value:
                        markdown_interpreter_related_enums.ActionTypeEnums.ACTION.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value:
                        markdown_interpreter_related_enums.AttackTypeEnums.MELEE_ATTACK.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.HIT_MODIFIER.value:
                        9,
                    markdown_interpreter_related_enums.ActionKeyEnums.RANGE.value:
                        5,
                    markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE.value:
                        "3d12 + 5",
                    markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE_TYPE.value:
                        markdown_interpreter_related_enums.DamageTypeEnums.PIERCING.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.NOTES.value:
                        "if it is a Large or smaller creature it is grappled (escape "
                        "DC 17). Until this grapple ends, the target is restrained, "
                        "and the troll can't use its bite attack on another target. "
                },
                {
                    markdown_interpreter_related_enums.ActionKeyEnums.NAME.value:
                        "Claw",
                    markdown_interpreter_related_enums.ActionKeyEnums.ACTION_TYPE.value:
                        markdown_interpreter_related_enums.ActionTypeEnums.ACTION.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value:
                        markdown_interpreter_related_enums.AttackTypeEnums.MELEE_ATTACK.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.HIT_MODIFIER.value:
                        9,
                    markdown_interpreter_related_enums.ActionKeyEnums.RANGE.value:
                        5,
                    markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE.value:
                        "2d6 + 5",
                    markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE_TYPE.value:
                        markdown_interpreter_related_enums.DamageTypeEnums.SLASHING.value
                },
                {
                    markdown_interpreter_related_enums.ActionKeyEnums.NAME.value:
                        "Swallow",
                    markdown_interpreter_related_enums.ActionKeyEnums.NOTES.value:
                        "The troll makes a bite attack against a creature it is grappling. If the attack hits, the target is swallowed, and the grapple ends. The swallowed creature is blinded and restrained, it has total cover against attacks and other effects outside the troll and it takes 10 (3d6) acid damage at the start of each of the troll's turns."
                        "The troll's gullet can hold one creature at a time. If the troll takes 20 damage or more on a single turn from a creature inside it, the troll must succeed on a DC 20 Constitution saving throw at the end of that turn or regurgitate the swallowed creature, which falls prone in a space within 10 feet of the troll. If the troll dies, a swallowed creature is no longer restrained by it and can escape from the corpse using 10 feet of movement, exiting prone. "
                },
                #keep this around and comment it out or in because you'll see this alot
                {
                    markdown_interpreter_related_enums.ActionKeyEnums.NAME.value:
                        "Multiattack",
                    markdown_interpreter_related_enums.ActionKeyEnums.ACTION_TYPE.value:
                        markdown_interpreter_related_enums.ActionTypeEnums.PASSIVE.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value:
                        markdown_interpreter_related_enums.AttackTypeEnums.UTILITY.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.NOTES.value:
                        "The troll makes four attacks: two with its bite and two with its claws."
                }
            ],
    }
