from kivymd.tools.patterns.create_project import temp_main

from A_GUI_programs.combat_sim.helper_functions.get_damage_and_get_chance_to_hit import get_chance_to_hit, get_damage
from A_GUI_programs.combat_sim.helper_functions.get_parsed_dict_from_dice_string import get_parsed_dict_from_dice_string
from universal_functions.enums import markdown_interpreter_related_enums


def _build_action_row_formatter(actions_list):
    """
    Scans all action dicts once and returns a function that formats a single
    action dict into an aligned
    "name : action_type : attack_type : hit_modifier : range : damage : damage_type"
    row, padded to the widest value seen in each column.

    claude made this
    """

    # these are all ordered in which they appear
    columns = \
        [
            markdown_interpreter_related_enums.ActionKeyEnums.NAME.value,
            markdown_interpreter_related_enums.ActionKeyEnums.ACTION_TYPE.value,
            markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value,
            # markdown_interpreter_related_enums.ActionKeyEnums.HIT_MODIFIER.value,
            # markdown_interpreter_related_enums.ActionKeyEnums.SAVE_DC.value,
            # markdown_interpreter_related_enums.ActionKeyEnums.SAVE_STAT.value,
            # markdown_interpreter_related_enums.ActionKeyEnums.RANGE.value,
            # markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE.value,
            # markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE_TYPE.value
        ]

    widths = {}
    for col in columns:
        max_width = len(col)
        for action in actions_list:
            """
            this _build function doesn't discriminate in it's renderings.
            so if a key is not present in a action which is in the columns list above.
            the function will piss and shit itself.

            unfortunately. i ran into the issue of the GUI breaking because the text rendered was too wise.
            """
            if col not in action:
                action[col] = "unknown"
            max_width = max(max_width, len(str(action[col])))
        widths[col] = max_width

    def format_header():
        return " : ".join(f"{col:<{widths[col]}}" for col in columns)

    def format_row(action):
        return " : ".join(f"{str(action[col]):<{widths[col]}}" for col in columns)

    return format_header, format_row


def actions_list_print_handler(
        attack_selection_menu_index: int,
        actions_list,
        executed_attack_bool,
        tab_amount: str):
    temp_action_menu_iterator_index = 0
    action_format_header, action_format_row = _build_action_row_formatter(actions_list)
    print(tab_amount, "\t\t ", action_format_header())
    for action in actions_list:
        if attack_selection_menu_index == temp_action_menu_iterator_index:
            print(tab_amount, "\t\t→", action_format_row(action))
            if executed_attack_bool:
                # if it's a martial attack
                if ((action[markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value]
                     ==
                     markdown_interpreter_related_enums.AttackTypeEnums.MELEE_ATTACK.value)
                        or
                        (action[markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value]
                         ==
                         markdown_interpreter_related_enums.AttackTypeEnums.RANGED_ATTACK.value)):

                    chance_to_hit = "unknown"
                    if markdown_interpreter_related_enums.ActionKeyEnums.HIT_MODIFIER.value in action:
                        # pass a simple string to int conversion, into a function. to get the chance to hit
                        chance_to_hit = get_chance_to_hit(
                            hit_modifier=int(
                                action[markdown_interpreter_related_enums.ActionKeyEnums.HIT_MODIFIER.value]),
                            tab_amount=tab_amount
                        )

                    damage = "unknown"
                    if markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE.value in action:
                        parsed_damage_dice_dict = get_parsed_dict_from_dice_string(
                            dice_string=action[
                                markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE.value],
                        )
                        damage = get_damage(
                            damage_dice=parsed_damage_dice_dict,
                            tab_amount=tab_amount
                        )

                    print(tab_amount+"\t\t\t", "chance to hit =", chance_to_hit)
                    print(tab_amount+"\t\t\t", "damage =", damage)
                    print(tab_amount+"\t\t\t", "damage_type =",
                          action[markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE_TYPE.value])
                    print(tab_amount+"\t\t\t", "range =", action[markdown_interpreter_related_enums.ActionKeyEnums.RANGE.value])

                # if it's a saving throw attack
                elif (action[markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value]
                      ==
                      markdown_interpreter_related_enums.AttackTypeEnums.SAVING_THROW.value):

                    print(tab_amount+"\t\t\t", "save_stat =",
                          action[markdown_interpreter_related_enums.ActionKeyEnums.SAVE_STAT.value])
                    print(tab_amount+"\t\t\t", "save_dc =",
                          action[markdown_interpreter_related_enums.ActionKeyEnums.SAVE_DC.value])
                    print(tab_amount+"\t\t\t", "damage =", get_damage
                        (
                        damage_dice=get_parsed_dict_from_dice_string
                            (
                            dice_string=action[markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE.value]
                        ),
                        tab_amount=tab_amount
                    )
                          )
                    print(tab_amount+"\t\t\t", "damage_type =",
                          action[markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE_TYPE.value])
                    print(tab_amount+"\t\t\t", "range =", action[markdown_interpreter_related_enums.ActionKeyEnums.RANGE.value])

                # if it's auto-hit
                elif (action[markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value]
                      ==
                      markdown_interpreter_related_enums.AttackTypeEnums.AUTO_HIT.value):

                    print(tab_amount+"\t\t\t", "This is a auto-hit attack so it just hits it's target")
                    print(tab_amount+"\t\t\t", "damage =", get_damage
                        (
                        damage_dice=get_parsed_dict_from_dice_string
                            (
                            dice_string=action[markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE.value]
                        ),
                        tab_amount=tab_amount
                    )
                          )
                    print(tab_amount+"\t\t\t", "damage_type =",
                          action[markdown_interpreter_related_enums.ActionKeyEnums.DAMAGE_TYPE.value])
                    print(tab_amount+"\t\t\t", "range =", action[markdown_interpreter_related_enums.ActionKeyEnums.RANGE.value])

                # if it's a utility / trait
                elif (action[markdown_interpreter_related_enums.ActionKeyEnums.ATTACK_TYPE.value]
                      ==
                      markdown_interpreter_related_enums.AttackTypeEnums.UTILITY.value):

                    print(tab_amount+"\t\t\t", "This is a utility, AKA aa trait. so there's no attack to execute.")

                else:
                    print(tab_amount+"\t\t\t", "The system cannot identify the attack_type this action has.")
        else:
            print(tab_amount, "\t\t ", action_format_row(action))
        temp_action_menu_iterator_index += 1
