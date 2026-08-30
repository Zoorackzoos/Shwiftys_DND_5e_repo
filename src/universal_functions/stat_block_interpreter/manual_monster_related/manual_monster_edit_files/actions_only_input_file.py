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
            'Devil, Chain',
        spreadsheet_enums.SpreadsheetKeysEnums.ACTIONS.value :
            [
                #------------------------TRAITS START -----------------------
                {
                    markdown_interpreter_related_enums.ActionKeyEnums.NAME.value:
                        "Devil's Sight",
                    markdown_interpreter_related_enums.ActionKeyEnums.ACTION_TYPE.value:
                        markdown_interpreter_related_enums.ActionTypeEnums.PASSIVE.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value:
                        markdown_interpreter_related_enums.AttackTypeEnums.UTILITY.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.NOTES.value:
                        "Magical darkness doesn't impede the devil's darkvision."
                },
                {
                    markdown_interpreter_related_enums.ActionKeyEnums.NAME.value:
                        "Magic Resistance",
                    markdown_interpreter_related_enums.ActionKeyEnums.ACTION_TYPE.value:
                        markdown_interpreter_related_enums.ActionTypeEnums.PASSIVE.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value:
                        markdown_interpreter_related_enums.AttackTypeEnums.UTILITY.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.NOTES.value:
                        "The devil has advantage on saving throws against spells and other magical effects."
                },
                # ------------------------TRAITS END -----------------------
                {
                    markdown_interpreter_related_enums.ActionKeyEnums.NAME.value:
                        "Chain",
                    markdown_interpreter_related_enums.ActionKeyEnums.ACTION_TYPE.value:
                        markdown_interpreter_related_enums.ActionTypeEnums.ACTION.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value:
                        markdown_interpreter_related_enums.AttackTypeEnums.MELEE_ATTACK.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.HIT_MODIFIER.value:
                        8,
                    markdown_interpreter_related_enums.ActionKeyEnums.RANGE.value:
                        10,
                    markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE.value:
                        "2d6 + 4",
                    markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE_TYPE.value:
                        markdown_interpreter_related_enums.DamageTypeEnums.SLASHING.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.NOTES.value:
                        "The target is grappled (escape DC 14) if the devil isn't already grappling a creature. Until this grapple ends, the target is restrained and takes 7 (2d6) piercing damage at the start of each of its turns."
                },
                {
                    markdown_interpreter_related_enums.ActionKeyEnums.NAME.value:
                        "Animate Chains",
                    markdown_interpreter_related_enums.ActionKeyEnums.ACTION_TYPE.value:
                        markdown_interpreter_related_enums.ActionTypeEnums.RECHARGEABLE_ACTION.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value:
                        markdown_interpreter_related_enums.AttackTypeEnums.UTILITY.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.NOTES.value:
                        "Up to four chains the devil can see within 60 feet of it magically sprout razor-­edged barbs and animate under the devil's control, provided that the chains aren't being worn or carried."
                        "Each animated chain is an object with AC 20, 20 hit points, resistance to piercing damage, and immunity to psychic and thunder damage. When the devil uses multiattack on its turn, it can use each animated chain to make one additional chain attack. An animated chain can grapple one creature of its own but can't make attacks while grappling. An animated chain reverts to its inanimate state if reduced to 0 hit points or if the devil is incapacitated or dies."
                },
                {
                    markdown_interpreter_related_enums.ActionKeyEnums.NAME.value:
                        "Unnerving Mask",
                    markdown_interpreter_related_enums.ActionKeyEnums.ACTION_TYPE.value:
                        markdown_interpreter_related_enums.ActionTypeEnums.PASSIVE.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value:
                        markdown_interpreter_related_enums.AttackTypeEnums.SAVING_THROW.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.SAVE_DC.value:
                        14,
                    markdown_interpreter_related_enums.ActionKeyEnums.SAVE_STAT:
                        spreadsheet_enums.SpreadsheetKeysEnums.WIS.value,
                    markdown_interpreter_related_enums.ActionKeyEnums.RANGE.value:
                        30,
                    markdown_interpreter_related_enums.ActionKeyEnums.NOTES.value:
                        "When a creature the devil can see starts its turn within 30 feet of the devil, the devil can create the illusion that it looks like one of the creature's departed loved ones or bitter enemies. If the creature can see the devil, it must succeed on a DC 14 Wisdom saving throw or be frightened until the end of its turn."
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
                        "The devil makes two attacks with its chains."
                }
            ],
    }
