# Template Monster, Parser Trial

# metadata

name: Template Monster, Parser Trial  
cr: 0.5  
url: [Example Stat Block](https://example.com/stat-block)  
font: DND\_5E\_CR\_versus\_player\_calculator  
author: Codex

# core stats

size: small  
type: construct  
alignment: almost chaos  
hp: 13  
ac: 12  
speed: 30, climb 20

# ability scores

str\_numeric\_stat: 8  
str\_modifier: \-1  
dex\_numeric\_stat: 14  
dex\_modifier: 2  
con\_numeric\_stat: 10  
con\_modifier: 0  
int\_numeric\_stat: 6  
int\_modifier: \-2  
wis\_numeric\_stat: 9  
wis\_modifier: \-1  
cha\_numeric\_stat: 4  
cha\_modifier: \-3

# saving throws

str: \-1  
dex: 4

# skills

stealth: 4  
history: \-2

# WRI

weak: radiant  
resistant: fire, necrotic  
immune: poison

# Senses

passive\_perception: 9  
senses: darkvision 60

# languages

* common  
* thieves cant

## cr inputs

average\_damage: 5.5  
attack\_modifier: 4  
has\_legendary\_action: false  
legendary\_action\_damage: 0  
has\_flight: false  
resistance\_count: 2  
immunity\_count: 1  
weakness\_count: 1  
save\_dc: 11  
is\_spellcaster: false  
regeneration\_per\_round: 0  
multiattack\_count: 0  
ability\_count: 1  
ability\_cr\_weight: 2  
recharge\_damage: 0  
limited\_use\_damage: 6  
bonus\_action\_damage: 1

# actions

## action \- test [spark](https://example.com/spark)

action\_type: action  
attack\_type: ranged\_spell\_attack  
hit\_modifier: 4  
damage: 1d6 \+ 2  
damage\_type: fire  
range: 60  
notes: Link in the action name should become plain text.

## action \- bad math shove

action\_type: bonus\_action  
attack\_type: saving\_throw  
save\_dc: 11  
save\_stat: str  
damage: 1d4 \- 1  
damage\_type: bludgeoning  
range: 5  
notes: Negative constants should not scare the parser.

# jokes i refuse to delete

This section is deliberately weird and should be ignored by the interpreter.  
chaos\_value: bananas

# lore

This monster exists to make sure the parser can ignore creative prose while still reading structured stat data.

# math description

Parser Trial (Definition)  
Purpose: Make future stat block parsing less fragile.  
