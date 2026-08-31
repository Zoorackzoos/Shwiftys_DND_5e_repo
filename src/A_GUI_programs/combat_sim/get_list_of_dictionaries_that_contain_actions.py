import ast


def get_list_of_dictionaries_that_contain_actions(
        incoming_list_of_dictionaries_that_contain_actions_string,
        tab_amount=""
):
    """
    in order to properly get the stored values of a monster's actions
    i need to parse them because everything in the spreadsheet is a string. no matter what.
        kind of puts the validity of having the database in a spreadsheet in question.
        but:
            1. who cares
            2. i'm too car in to change it
            3. this is low scale in terms of database columns and rows
            4. spreadsheets are more user centric so hypothetically someone could spit out
                a completely different spreadsheet and as long as they had most of the
                keys this program uses, it would be compatible.

    example input:
    "[
        {
            'name': 'Scimitar',
            'action_type': 'action',
            'attack_type': 'melee_attack',
            'hit_modifier': 4,
            'range': 5,
            'damage': '1d6 + 2',
            'damage_type': 'slashing'
        },
        {
            'name': 'shortbow',
            'action_type': 'action',
            'attack_type': 'ranged_attack',
            'hit_modifier': 4,
            'range': 80,
            'damage': '1d6 + 2',
            'damage_type': 'piercing'
        }
    ]"
        all this is a string
        to the.... non string versoin of that.
        it returns the list that contins dicitonaries

    "have you tried ast.literal_eval ?"
        -chat gpt
    thanks chat 🥀🥀🥀

    :param incoming_list_of_dictionaries_that_contain_actions_string:
    :param tab_amount:
    :return:
    """
    print(
        tab_amount,
        "get_list_of_dictionaries_that_contain_actions"
    )

    return_list_of_dicts_that_contain_actions = \
        ast.literal_eval(
            incoming_list_of_dictionaries_that_contain_actions_string
        )

    return return_list_of_dicts_that_contain_actions

if __name__ == "__main__":
    # "Goblin" actions
    example_string = "[{'name': 'Scimitar', 'action_type': 'action', 'attack_type': 'melee_attack', 'hit_modifier': 4, 'range': 5, 'damage': '1d6 + 2', 'damage_type': 'slashing'}, {'name': 'shortbow', 'action_type': 'action', 'attack_type': 'ranged_attack', 'hit_modifier': 4, 'range': 80, 'damage': '1d6 + 2', 'damage_type': 'piercing'}]"

    print(type(example_string))
    print(example_string)

    print()

    example_string_put_thru_function = get_list_of_dictionaries_that_contain_actions(
                    incoming_list_of_dictionaries_that_contain_actions_string=example_string
                )
    print(type(example_string_put_thru_function))
    print(example_string_put_thru_function)