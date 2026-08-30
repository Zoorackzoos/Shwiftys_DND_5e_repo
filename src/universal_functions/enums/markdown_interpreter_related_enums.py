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

class ActionKeyEnums(Enum):
    NAME = "name"
    ACTION_TYPE = "action_type"
    ATTACK_TYPE = "attack_type"

    # martial attacks only
    HIT_MODIFIER = "hit_modifier"
    # magic or whatever else only
    SAVE_DC = "save_dc"
    SAVE_STAT = "save_stat"

    DAMAGE = "damage"
    DAMAGE_TYPE = "damage_type"
    RANGE = "range"
    NOTES = "notes"


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
    AUTO_HIT = "auto_hit" # this is used for magic missile and it's derivatives

#TODO: think about how you structure your enums in this repo's directory.
class DamageTypeEnums(Enum):
    SLASHING = "slashing"
    PIERCING = "piercing"
    BLUDGEONING = "bludgeoning"
    COLD = "cold"
    POISON = "poison"
    ACID = "acid"
    PSYCHIC = "psychic"
    FIRE = "fire"
    NECROTIC = "necrotic"
    RADIANT = "radiant"
    FORCE = "force"
    THUNDER = "thunder"
    LIGHTNING = "lightning"
    