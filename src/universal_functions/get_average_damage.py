# src/universal_functions/get_average_damage.py

def get_average_damage(dice_dict, tab_amount="\t"):
    """
    2d6
    7.0

    2d4 + 1d8
    9.5

    5d4 + 2
    29

    store like dictionary
    damage_dice_var = {
        6 : 2
        "constant" : 2
    }

    previous:
        total = 0
        matches = re.findall(r"(\\d+)d(\\d+)", dice_string)
        for dice_count, dice_sides in matches:
            dice_count = int(dice_count)
            dice_sides = int(dice_sides)
            average_die = (dice_sides + 1) / 2
            total += dice_count * average_die

    """
    print(tab_amount,"get_damage_per_round")
    tab_amount += "\t"

    total = 0

    for key,value in dice_dict.items():
        if key == "constant":
            total += value
        else:
            print(tab_amount+"\t",key,":",value)
            average_die = (key + 1) / 2
            print(tab_amount+"\t\t","average_die =",average_die)
            total += value * average_die
            print(tab_amount+"\t\t","total =",total)

    print(tab_amount+"\t","total =",total)
    return total

def get_average_damage_no_print(dice_dict):
    total = 0

    for key,value in dice_dict.items():
        if key == "constant":
            total += value
        else:
            average_die = (key + 1) / 2
            total += value * average_die

    return total

if __name__ == "__main__":
    tab_amount = "\t"
    dice_dict = \
        {
            4 : 8,
            6 : 0,
            8 : 0,
            10 : 0,
            12 : 3,
            20 : 0,
            "constant" : 8
        }

    average_damage = (get_average_damage
    (
        dice_dict=dice_dict,
        tab_amount=tab_amount
    ))

    print("average_damage =",average_damage)

