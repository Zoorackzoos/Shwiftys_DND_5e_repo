"""
This has questionable uses.
1. it can be used to show users (me) what I am required to put in certain fields
    when making markdown stat blocks in order to maintain consistency.
2. the system can use these enums instead of strings which is better for consistency.

most of the field enums like:
* CR
* size
* type
will not be placed here. they are in "spreadsheet_enums.py"
"""
from enum import Enum

class ActionTypeEnums(Enum):
    ACTION = "action"
    BONUS_ACTION = "bonus_action"
    REACTION = "reaction"

    RECHARGEABLE_ACTION = "rechargeable_action"
    RECHARGEABLE_BONUS_ACTION = "rechargeable_bonus_action"
    RECHARGEABLE_REACTION = "rechargeable_reaction"

    LIMITED_USE_ACTION = "limited_use_action"
    LIMITED_USE_BONUS_ACTION = "limited_use_bonus_action"
    LIMITED_USE_REACTION = "limited_use_reaction"

    PASSIVE = "passive"

class AttackTypeEnums(Enum):
    MELEE_ATTACK = "melee_attack"
    RANGED_ATTACK = "ranged_attack"
    SAVING_THROW = "saving_throw"
    UTILITY = "utility"
    AUTO_HIT = "auto_hit" # this is used for magic missle and it's dervatives