import random


def get_chance_to_hit(hit_modifier,tab_amount="\t"):
    """
    gets number from 1 to 20 (a d210)
    then adds the hit_modifier onto that number.

    :param hit_modifier:
    :param tab_amount:
    :return:
    """
    #print(tab_amount,"get_chance_to_hit")
    tab_amount += "\t"
    rolled_dice_to_hit = random.randint(1,20)
    #print(tab_amount,"rolled_dice_to_hit =",rolled_dice_to_hit)
    adjusted_rolled_dice_to_hit = rolled_dice_to_hit+hit_modifier
    #print(tab_amount,"rolled_dice_to_hit + modifier =",adjusted_rolled_dice_to_hit)
    return adjusted_rolled_dice_to_hit

def get_damage(damage_dice,tab_amount="\t"):
    #print(tab_amount,"get_damage")
    tab_amount += "\t"

    total_damage = 0

    for key, value in damage_dice.items():
        if key == "constant":
            #print(tab_amount, "constant damage =", value)
            total_damage += value
        elif value == 0:
            #print(tab_amount,"no",key,"dice present. not rolling")
            pass
        else:
            #print(tab_amount,"found",key)
            for i in range(value):
                incoming_damage = random.randint(1,int(key))
                #print(tab_amount+"\t","incoming_damage =",incoming_damage)
                total_damage += incoming_damage

    return total_damage

if __name__ == "__main__":
    print("program started")
    tab_amount = "\t"
    hit_modifier = 6
    damage_dice = \
        {
            20 : 0,
            12 : 0,
            10 : 0,
            8 : 0,
            6 : 2,
            4 : 0,
            "constant" : 6
        }
    chance_to_hit = get_chance_to_hit(hit_modifier=hit_modifier,tab_amount=tab_amount)
    damage = get_damage(damage_dice=damage_dice,tab_amount=tab_amount)

    print(tab_amount,"chance_to_hit =",chance_to_hit)
    print(tab_amount,"damage =",damage)

    print("program ended")
