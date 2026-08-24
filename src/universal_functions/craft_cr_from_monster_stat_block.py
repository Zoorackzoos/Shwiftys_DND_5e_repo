# =====================================================
# D&D 5E Monster CR Calculator
# Based on the 2014 DMG monster creation math.
# =====================================================
from src.universal_functions.vars import spreadsheet_enums

CR_TABLE = [
    {"CR": 0, "hp_min": 1, "hp_max": 6, "dpr_min": 0, "dpr_max": 1, "ac": 13, "attack_bonus": 3, "save_dc": 13},
    {"CR": 0.125, "hp_min": 7, "hp_max": 35, "dpr_min": 2, "dpr_max": 3, "ac": 13, "attack_bonus": 3, "save_dc": 13},
    {"CR": 0.25, "hp_min": 36, "hp_max": 49, "dpr_min": 4, "dpr_max": 5, "ac": 13, "attack_bonus": 3, "save_dc": 13},
    {"CR": 0.5, "hp_min": 50, "hp_max": 70, "dpr_min": 6, "dpr_max": 8, "ac": 13, "attack_bonus": 3, "save_dc": 13},
    {"CR": 1, "hp_min": 71, "hp_max": 85, "dpr_min": 9, "dpr_max": 14, "ac": 13, "attack_bonus": 3, "save_dc": 13},
    {"CR": 2, "hp_min": 86, "hp_max": 100, "dpr_min": 15, "dpr_max": 20, "ac": 13, "attack_bonus": 3, "save_dc": 13},
    {"CR": 3, "hp_min": 101, "hp_max": 115, "dpr_min": 21, "dpr_max": 26, "ac": 13, "attack_bonus": 4, "save_dc": 13},
    {"CR": 4, "hp_min": 116, "hp_max": 130, "dpr_min": 27, "dpr_max": 32, "ac": 14, "attack_bonus": 5, "save_dc": 14},
    {"CR": 5, "hp_min": 131, "hp_max": 145, "dpr_min": 33, "dpr_max": 38, "ac": 15, "attack_bonus": 6, "save_dc": 15},
    {"CR": 6, "hp_min": 146, "hp_max": 160, "dpr_min": 39, "dpr_max": 44, "ac": 15, "attack_bonus": 6, "save_dc": 15},
    {"CR": 7, "hp_min": 161, "hp_max": 175, "dpr_min": 45, "dpr_max": 50, "ac": 15, "attack_bonus": 6, "save_dc": 15},
    {"CR": 8, "hp_min": 176, "hp_max": 190, "dpr_min": 51, "dpr_max": 56, "ac": 16, "attack_bonus": 7, "save_dc": 16},
    {"CR": 9, "hp_min": 191, "hp_max": 205, "dpr_min": 57, "dpr_max": 62, "ac": 16, "attack_bonus": 7, "save_dc": 16},
    {"CR": 10, "hp_min": 206, "hp_max": 220, "dpr_min": 63, "dpr_max": 68, "ac": 17, "attack_bonus": 7, "save_dc": 16},
    {"CR": 11, "hp_min": 221, "hp_max": 235, "dpr_min": 69, "dpr_max": 74, "ac": 17, "attack_bonus": 8, "save_dc": 17},
    {"CR": 12, "hp_min": 236, "hp_max": 250, "dpr_min": 75, "dpr_max": 80, "ac": 17, "attack_bonus": 8, "save_dc": 18},
    {"CR": 13, "hp_min": 251, "hp_max": 265, "dpr_min": 81, "dpr_max": 86, "ac": 18, "attack_bonus": 8, "save_dc": 18},
    {"CR": 14, "hp_min": 266, "hp_max": 280, "dpr_min": 87, "dpr_max": 92, "ac": 18, "attack_bonus": 8, "save_dc": 18},
    {"CR": 15, "hp_min": 281, "hp_max": 295, "dpr_min": 93, "dpr_max": 98, "ac": 18, "attack_bonus": 8, "save_dc": 18},
    {"CR": 16, "hp_min": 296, "hp_max": 310, "dpr_min": 99, "dpr_max": 104, "ac": 18, "attack_bonus": 9, "save_dc": 18},
    {"CR": 17, "hp_min": 311, "hp_max": 325, "dpr_min": 105, "dpr_max": 110, "ac": 19, "attack_bonus": 10, "save_dc": 19},
    {"CR": 18, "hp_min": 326, "hp_max": 340, "dpr_min": 111, "dpr_max": 116, "ac": 19, "attack_bonus": 10, "save_dc": 19},
    {"CR": 19, "hp_min": 341, "hp_max": 355, "dpr_min": 117, "dpr_max": 122, "ac": 19, "attack_bonus": 10, "save_dc": 19},
    {"CR": 20, "hp_min": 356, "hp_max": 400, "dpr_min": 123, "dpr_max": 140, "ac": 19, "attack_bonus": 10, "save_dc": 19},
    {"CR": 21, "hp_min": 401, "hp_max": 445, "dpr_min": 141, "dpr_max": 158, "ac": 19, "attack_bonus": 11, "save_dc": 20},
    {"CR": 22, "hp_min": 446, "hp_max": 490, "dpr_min": 159, "dpr_max": 176, "ac": 19, "attack_bonus": 11, "save_dc": 20},
    {"CR": 23, "hp_min": 491, "hp_max": 535, "dpr_min": 177, "dpr_max": 194, "ac": 19, "attack_bonus": 11, "save_dc": 20},
    {"CR": 24, "hp_min": 536, "hp_max": 580, "dpr_min": 195, "dpr_max": 212, "ac": 19, "attack_bonus": 12, "save_dc": 21},
    {"CR": 25, "hp_min": 581, "hp_max": 625, "dpr_min": 213, "dpr_max": 230, "ac": 19, "attack_bonus": 12, "save_dc": 21},
    {"CR": 26, "hp_min": 626, "hp_max": 670, "dpr_min": 231, "dpr_max": 248, "ac": 19, "attack_bonus": 12, "save_dc": 21},
    {"CR": 27, "hp_min": 671, "hp_max": 715, "dpr_min": 249, "dpr_max": 266, "ac": 19, "attack_bonus": 13, "save_dc": 22},
    {"CR": 28, "hp_min": 716, "hp_max": 760, "dpr_min": 267, "dpr_max": 284, "ac": 19, "attack_bonus": 13, "save_dc": 22},
    {"CR": 29, "hp_min": 761, "hp_max": 805, "dpr_min": 285, "dpr_max": 302, "ac": 19, "attack_bonus": 13, "save_dc": 22},
    {"CR": 30, "hp_min": 806, "hp_max": 850, "dpr_min": 303, "dpr_max": 320, "ac": 19, "attack_bonus": 14, "save_dc": 23},
]


def fail_cr_calculation(error_message, tab_amount="\t"):
    print(tab_amount, "ERROR:", error_message)
    raise SystemExit(1)


def get_cr_index(cr):
    for index, row in enumerate(CR_TABLE):
        if row["CR"] == cr:
            return index

    return len(CR_TABLE) - 1


def get_cr_from_index(index):
    safe_index = max(0, min(len(CR_TABLE) - 1, int(index + 0.5)))
    return CR_TABLE[safe_index]["CR"]


def get_expected_values_from_cr(cr, tab_amount="\t"):
    print(tab_amount, "get_expected_values_from_cr")

    for row in CR_TABLE:
        if row["CR"] == cr:
            return row

    fail_cr_calculation(
        error_message="Could not find expected values for CR " + str(cr),
        tab_amount=tab_amount + "\t"
    )


def get_defensive_cr(hit_points, tab_amount="\t"):
    print(tab_amount, "get_defensive_cr")

    for row in CR_TABLE:
        if row["hp_min"] <= hit_points <= row["hp_max"]:
            return row["CR"]

    if hit_points <= 0:
        fail_cr_calculation(
            error_message="Hit points must be greater than 0.",
            tab_amount=tab_amount + "\t"
        )

    fail_cr_calculation(
        error_message="Hit points are outside the supported CR 0-30 table: " + str(hit_points),
        tab_amount=tab_amount + "\t"
    )


def get_offensive_cr(damage_per_round, tab_amount="\t"):
    print(tab_amount, "get_offensive_cr")
    tab_amount += "\t"
    print(tab_amount,"damage_per_round:",damage_per_round)

    rounded_damage_per_round = int(damage_per_round)

    for row in CR_TABLE:
        print(tab_amount,row["dpr_min"],"<=",rounded_damage_per_round,"<=",row["dpr_max"])
        if row["dpr_min"] <= rounded_damage_per_round <= row["dpr_max"]:
            print(tab_amount+"\t","this one :-3")
            print(tab_amount+"\t","returning -->",row["CR"],"")
            return row["CR"]

    if rounded_damage_per_round < 0:
        fail_cr_calculation(
            error_message="Damage per round cannot be negative.",
            tab_amount=tab_amount + "\t"
        )

    #canary :-3
    fail_cr_calculation(
        error_message="Damage per round is outside the supported CR 0-30 table: " + str(damage_per_round),
        tab_amount=tab_amount + "\t"
    )


def adjust_cr_by_stat_difference(starting_cr, actual_value, expected_value, label, tab_amount="\t"):
    print(tab_amount, "adjust_cr_by_stat_difference")
    print(tab_amount + "\t", "label =", label)
    print(tab_amount + "\t", "starting_cr =", starting_cr)
    print(tab_amount + "\t", "actual_value =", actual_value)
    print(tab_amount + "\t", "expected_value =", expected_value)

    difference = actual_value - expected_value
    cr_step_adjustment = int(difference / 2)
    adjusted_cr = get_cr_from_index(get_cr_index(starting_cr) + cr_step_adjustment)

    print(tab_amount + "\t", "difference =", difference)
    print(tab_amount + "\t", "cr_step_adjustment =", cr_step_adjustment)
    print(tab_amount + "\t", "adjusted_cr =", adjusted_cr)

    return adjusted_cr


def get_hp_multiplier_from_defenses(defensive_cr, resistance_count, immunity_count, tab_amount="\t"):
    print(tab_amount, "get_hp_multiplier_from_defenses")

    has_resistance = resistance_count > 0
    has_immunity = immunity_count > 0

    print(tab_amount + "\t", "defensive_cr =", defensive_cr)
    print(tab_amount + "\t", "resistance_count =", resistance_count)
    print(tab_amount + "\t", "immunity_count =", immunity_count)

    if not has_resistance and not has_immunity:
        print(tab_amount + "\t", "hp_multiplier = 1")
        return 1

    if defensive_cr <= 4:
        hp_multiplier = 2
    elif defensive_cr <= 10:
        hp_multiplier = 2 if has_immunity else 1.5
    elif defensive_cr <= 16:
        hp_multiplier = 1.5 if has_immunity else 1.25
    else:
        hp_multiplier = 1.25 if has_immunity else 1

    print(tab_amount + "\t", "hp_multiplier =", hp_multiplier)
    return hp_multiplier


def craft_cr_from_monster_stat_block(
        hit_points,
        armor_class,
        average_damage,
        attack_modifier=0,
        has_legendary_action=False,
        has_flight=False,
        resistance_count=0,
        immunity_count=0,
        weakness_count=0,
        save_dc=0,
        is_spellcaster=False,
        regeneration_per_round=0,
        multiattack_count=0,
        ability_count=0,
        recharge_damage=0,
        limited_use_damage=0,
        bonus_action_damage=0,
        legendary_action_damage=0,
        ability_cr_weight=2,
        tab_amount="\t"
):
    print(tab_amount, "craft_cr_from_monster_stat_block")
    tab_amount += "\t"

    if hit_points <= 0:
        fail_cr_calculation("Hit points must be greater than 0.", tab_amount)
    if armor_class <= 0:
        fail_cr_calculation("Armor class must be greater than 0.", tab_amount)
    if average_damage < 0:
        fail_cr_calculation("Damage per round cannot be negative.", tab_amount)

    original_hit_points = hit_points
    original_damage_per_round = average_damage

    # -------------------------------
    # Defensive CR
    # -------------------------------
    print(tab_amount, "Defensive CR")

    if regeneration_per_round > 0:
        print(tab_amount + "\t", "regeneration_per_round =", regeneration_per_round)
        print(tab_amount + "\t", "before: hit_points =", hit_points)
        hit_points += regeneration_per_round * 3
        print(tab_amount + "\t", "after: hit_points =", hit_points)

    if has_flight:
        print(tab_amount + "\t", "has_flight =", has_flight)
        print(tab_amount + "\t", "before: hit_points =", hit_points)
        hit_points *= 1.25
        print(tab_amount + "\t", "after: hit_points =", hit_points)

    preliminary_defensive_cr = get_defensive_cr(
        hit_points=hit_points,
        tab_amount=tab_amount + "\t"
    )
    print(tab_amount + "\t", "preliminary_defensive_cr =", preliminary_defensive_cr)

    hp_multiplier = get_hp_multiplier_from_defenses(
        defensive_cr=preliminary_defensive_cr,
        resistance_count=resistance_count,
        immunity_count=immunity_count,
        tab_amount=tab_amount + "\t"
    )

    if hp_multiplier != 1:
        print(tab_amount + "\t", "before defense multiplier: hit_points =", hit_points)
        hit_points *= hp_multiplier
        print(tab_amount + "\t", "after defense multiplier: hit_points =", hit_points)

    if weakness_count > 0:
        print(tab_amount + "\t", "weakness_count =", weakness_count)
        print(tab_amount + "\t", "before weakness adjustment: hit_points =", hit_points)
        hit_points *= 0.5
        print(tab_amount + "\t", "after weakness adjustment: hit_points =", hit_points)

    defensive_cr = get_defensive_cr(
        hit_points=hit_points,
        tab_amount=tab_amount + "\t"
    )
    print(tab_amount + "\t", "defensive_cr_from_effective_hp =", defensive_cr)

    defensive_stats = get_expected_values_from_cr(
        cr=defensive_cr,
        tab_amount=tab_amount + "\t"
    )
    defensive_cr = adjust_cr_by_stat_difference(
        starting_cr=defensive_cr,
        actual_value=armor_class,
        expected_value=defensive_stats["ac"],
        label="armor_class",
        tab_amount=tab_amount + "\t"
    )

    # -------------------------------
    # Offensive CR
    # -------------------------------
    print(tab_amount, "Offensive CR")

    if multiattack_count > 0:
        print(tab_amount + "\t", "multiattack_count =", multiattack_count)
        print(tab_amount + "\t", "before: damage_per_round =", average_damage)
        average_damage *= multiattack_count
        print(tab_amount + "\t", "after: damage_per_round =", average_damage)

    if recharge_damage > 0:
        recharge_dpr = recharge_damage / 3
        print(tab_amount + "\t", "recharge_damage =", recharge_damage)
        print(tab_amount + "\t", "recharge_dpr =", recharge_dpr)
        average_damage += recharge_dpr
        print(tab_amount + "\t", "after recharge: damage_per_round =", average_damage)

    if limited_use_damage > 0:
        limited_use_dpr = limited_use_damage / 3
        print(tab_amount + "\t", "limited_use_damage =", limited_use_damage)
        print(tab_amount + "\t", "limited_use_dpr =", limited_use_dpr)
        average_damage += limited_use_dpr
        print(tab_amount + "\t", "after limited use: damage_per_round =", average_damage)

    if bonus_action_damage > 0:
        print(tab_amount + "\t", "bonus_action_damage =", bonus_action_damage)
        average_damage += bonus_action_damage
        print(tab_amount + "\t", "after bonus action: damage_per_round =", average_damage)

    if legendary_action_damage > 0:
        print(tab_amount + "\t", "legendary_action_damage =", legendary_action_damage)
        average_damage += legendary_action_damage
        print(tab_amount + "\t", "after legendary action damage: damage_per_round =", average_damage)
    elif has_legendary_action:
        print(tab_amount + "\t", "has_legendary_action =", has_legendary_action)
        print(tab_amount + "\t", "before legendary action estimate: damage_per_round =", average_damage)
        average_damage *= 1.25
        print(tab_amount + "\t", "after legendary action estimate: damage_per_round =", average_damage)

    if ability_count > 0:
        print(tab_amount + "\t", "ability_count =", ability_count)
        print(tab_amount + "\t", "ability_cr_weight =", ability_cr_weight)
        print(tab_amount + "\t", "before ability estimate: damage_per_round =", average_damage)
        average_damage += ability_count * ability_cr_weight
        print(tab_amount + "\t", "after ability estimate: damage_per_round =", average_damage)

    if is_spellcaster:
        print(tab_amount + "\t", "is_spellcaster =", is_spellcaster)
        print(tab_amount + "\t", "No direct multiplier was applied. Put spell damage into damage_per_round or ability damage fields.")

    offensive_cr = get_offensive_cr(
        damage_per_round=average_damage,
        tab_amount=tab_amount + "\t"
    )
    print(tab_amount + "\t", "offensive_cr_from_damage =", offensive_cr)

    offensive_stats = get_expected_values_from_cr(
        cr=offensive_cr,
        tab_amount=tab_amount + "\t"
    )
    print(tab_amount + "\t", "offensive_stats =", offensive_stats)

    if save_dc > 0:
        offensive_cr_from_attack_bonus = adjust_cr_by_stat_difference(
            starting_cr=offensive_cr,
            actual_value=attack_modifier,
            expected_value=offensive_stats["attack_bonus"],
            label="attack_bonus",
            tab_amount=tab_amount + "\t"
        )
        offensive_cr_from_save_dc = adjust_cr_by_stat_difference(
            starting_cr=offensive_cr,
            actual_value=save_dc,
            expected_value=offensive_stats["save_dc"],
            label="save_dc",
            tab_amount=tab_amount + "\t"
        )
        offensive_cr = max(offensive_cr_from_attack_bonus, offensive_cr_from_save_dc)
        print(tab_amount + "\t", "offensive_cr uses higher attack/save result =", offensive_cr)
    else:
        offensive_cr = adjust_cr_by_stat_difference(
            starting_cr=offensive_cr,
            actual_value=attack_modifier,
            expected_value=offensive_stats["attack_bonus"],
            label="attack_bonus",
            tab_amount=tab_amount + "\t"
        )

    # -------------------------------
    # Final CR
    # -------------------------------
    print(tab_amount, "Final CR")

    defensive_index = get_cr_index(defensive_cr)
    offensive_index = get_cr_index(offensive_cr)
    final_index = (defensive_index + offensive_index) / 2
    final_cr = get_cr_from_index(final_index)

    print(tab_amount + "\t", "original_hit_points =", original_hit_points)
    print(tab_amount + "\t", "effective_hit_points =", hit_points)
    print(tab_amount + "\t", "original_damage_per_round =", original_damage_per_round)
    print(tab_amount + "\t", "effective_damage_per_round =", average_damage)
    print(tab_amount + "\t", "defensive_cr =", defensive_cr)
    print(tab_amount + "\t", "offensive_cr =", offensive_cr)
    print(tab_amount + "\t", "final_cr =", final_cr)

    return final_cr


def plug_monster_var_values_into_get_cr_from_monster(monster_var, tab_amount="\t"):
    print(tab_amount, "plug_monster_var_values_into_get_cr_from_monster")
    tab_amount += "\t"

    def get_monster_value(spreadsheet_key, code_key, default_value=None):
        if spreadsheet_key in monster_var:
            return monster_var[spreadsheet_key]
        if code_key in monster_var:
            return monster_var[code_key]
        return default_value

    return craft_cr_from_monster_stat_block(
        hit_points=get_monster_value(spreadsheet_enums.SpreadsheetKeysEnums.HP.value, "hp"),
        armor_class=get_monster_value(spreadsheet_enums.SpreadsheetKeysEnums.AC.value, "ac"),
        average_damage=get_monster_value(spreadsheet_enums.SpreadsheetKeysEnums.AVERAGE_DAMAGE.value, "average_damage"),
        attack_modifier=get_monster_value(spreadsheet_enums.SpreadsheetKeysEnums.ATTACK_MODIFIER.value, "attack_modifier", 0),
        has_legendary_action=get_monster_value(spreadsheet_enums.SpreadsheetKeysEnums.HAS_LEGENDARY_ACTION.value, "has_legendary_action", False),
        has_flight=get_monster_value(spreadsheet_enums.SpreadsheetKeysEnums.HAS_FLIGHT.value, "has_flight", False),
        resistance_count=get_monster_value(spreadsheet_enums.SpreadsheetKeysEnums.RESISTANCE_COUNT.value, "resistance_count", 0),
        immunity_count=get_monster_value(spreadsheet_enums.SpreadsheetKeysEnums.IMMUNITY_COUNT.value, "immunity_count", 0),
        weakness_count=get_monster_value(spreadsheet_enums.SpreadsheetKeysEnums.WEAKNESS_COUNT.value, "weakness_count", 0),
        save_dc=get_monster_value(spreadsheet_enums.SpreadsheetKeysEnums.SAVE_DC.value, "save_dc", 0),
        is_spellcaster=get_monster_value(spreadsheet_enums.SpreadsheetKeysEnums.IS_SPELLCASTER.value, "is_spellcaster", False),
        regeneration_per_round=get_monster_value(spreadsheet_enums.SpreadsheetKeysEnums.REGENERATION_PER_ROUND.value, "regeneration_per_round", 0),
        multiattack_count=get_monster_value(spreadsheet_enums.SpreadsheetKeysEnums.MULTIATTACK_COUNT.value, "multiattack_count", 0),
        ability_count=get_monster_value(spreadsheet_enums.SpreadsheetKeysEnums.ABILITY_COUNT.value, "ability_count", 0),
        recharge_damage=get_monster_value(spreadsheet_enums.SpreadsheetKeysEnums.RECHARGE_DAMAGE.value, "recharge_damage", 0),
        limited_use_damage=get_monster_value(spreadsheet_enums.SpreadsheetKeysEnums.LIMITED_USE_DAMAGE.value, "limited_use_damage", 0),
        bonus_action_damage=get_monster_value(spreadsheet_enums.SpreadsheetKeysEnums.BONUS_ACTION_DAMAGE.value, "bonus_action_damage", 0),
        legendary_action_damage=get_monster_value(spreadsheet_enums.SpreadsheetKeysEnums.LEGENDARY_ACTION_DAMAGE.value, "legendary_action_damage", 0),
        ability_cr_weight=get_monster_value(spreadsheet_enums.SpreadsheetKeysEnums.ABILITY_CR_WEIGHT.value, "ability_cr_weight", 2),
        tab_amount=tab_amount
    )
