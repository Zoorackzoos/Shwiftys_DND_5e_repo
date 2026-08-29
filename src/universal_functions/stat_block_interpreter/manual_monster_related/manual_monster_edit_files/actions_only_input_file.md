# Dragon, Chromatic, Black, Young

# metadata
name: Dragon, Chromatic, Black, Young

# actions

## trait \- Amphibious
action_type: passive
attack_type: utility
notes: The dragon can breathe air and water.

## multiattack 
action_type: passive
attack_type: utility
notes: The dragon makes three attacks: one with its bite and two with its claws.

## action \- bite
action_type: action
attack_type: melee\_attack
hit_modifier: 7
range: 10
damage: 2d10 \+ 1d8 \+ 4 
damage_type: piercing

## action \- claw
action_type: action
attack_type: melee\_attack
hit_modifier: 7
range: 5 
damage: 2d6 \+ 4
damage_type: slashing

## rechargeable action \- Acid Breath
action_type: rechargeable\_action
attack_type: saving_throw
range: 30
save_dc: 14
save_stat: dex
damage: 11d8
damage_type: acid