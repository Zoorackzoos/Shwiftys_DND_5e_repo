# Verbose Template Monster 2, Overexplained Parser Trial

# metadata

name: Verbose Template Monster 2, Overexplained Parser Trial  
cr: ????  
url: \[Verbose Example Stat Block\](https://example.com/verbose-stat-block)  
font: DND\_5E\_CR\_versus\_player\_calculuator  
author: Codex  
additional: Interpreted from markdown with inferred CR helper values.

# core stats

size: medium  
type: humanoid  
alignment: neutral evil  
hp: 45  
ac: 15  
speed: 30, fly 40

# ability scores

str\_numeric\_stat: 8  
str\_modifier: \-1  
dex\_numeric\_stat: 16  
dex\_modifier: 3  
con\_numeric\_stat: 14  
con\_modifier: 2  
int\_numeric\_stat: 10  
int\_modifier: 0  
wis\_numeric\_stat: 12  
wis\_modifier: 1  
cha\_numeric\_stat: 6  
cha\_modifier: \-2

# saving throws

dex: 5  
wis: 3

# skills

acrobatics: 5  
stealth: 7  
history: \-1

# WRI

weak: radiant  
resistant: fire, necrotic  
immune: poison

# Senses

senses: darkvision 60  
passive\_perception: 11

# languages

\* common  
\* thieves cant

## cr inputs

These can be omitted or set to 0 when you want the generated Python file to infer them from actions, WRI, and speed.

average\_damage: 0  
attack\_modifier: 0  
has\_legendary\_action: false  
legendary\_action\_damage: 0  
has\_flight: false  
resistance\_count: 0  
immunity\_count: 0  
weakness\_count: 0  
save\_dc: 0  
is\_spellcaster: false  
regeneration\_per\_round: 0  
multiattack\_count: 0  
ability\_count: 0  
ability\_cr\_weight: 2  
recharge\_damage: 0  
limited\_use\_damage: 0  
bonus\_action\_damage: 0

# actions

## action \- reliable sword strike

action\_type: action  
attack\_type: melee\_attack  
hit\_modifier: 5  
damage: 2d8 \+ 3  
damage\_type: slashing  
range: 5  
notes: This should be considered for average\_damage.

## action \- weaker thrown dagger

action\_type: action  
attack\_type: ranged\_attack  
hit\_modifier: 5  
damage: 1d4 \+ 3  
damage\_type: piercing  
range: 20  
notes: The interpreter should prefer the stronger normal action above.

## bonus action \- wing clip

action\_type: bonus action  
attack\_type: melee\_attack  
hit\_modifier: 5  
damage: 1d6 \+ 3  
damage\_type: slashing  
range: 5  
notes: This should become bonus\_action\_damage.

## rechargeable action \- acid burst

action\_type: rechargeable action  
attack\_type: saving\_throw  
save\_dc: 13  
save\_stat: dex  
damage: 4d6  
damage\_type: acid  
range: 30  
notes: This should become recharge\_damage and save\_dc.

## limited use reaction \- spiteful spark

action\_type: limited use reaction  
attack\_type: saving\_throw  
save\_dc: 13  
save\_stat: wis  
damage: 2d6  
damage\_type: lightning  
range: 30  
notes: This should become limited\_use\_damage.

## passive \- mean aura

action\_type: passive  
attack\_type: utility  
range: 10  
notes: This has no damage, so it can count as a utility ability.

# lore

Put freeform monster description here. The interpreter should not try to understand this section.