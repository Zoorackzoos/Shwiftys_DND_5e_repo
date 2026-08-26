from enum import Enum

class SpreadsheetKeysEnums(Enum):
    """
    These are if you want to call a dictionary's key.
    they're here in order to make sure you don't get a type error because you put
    "size" instead of "Size" or something.
    this makes more sense in a java context but having to go to the spreadsheet to confirm
    the right spelling is dumb asf. \n

    if you want the value these enums store, you have to have ".value" on the end. :---)
    """
    NAME = "Name"
    SIZE = "Size"
    TYPE = "Type"
    CR = "CR"
    URL = "URL"
    FONT = "Font"
    AUTHOR = "Author"
    AC = "AC"
    HP = "HP"
    SPEEDS = "Speeds"
    ALIGN = "Align."
    STR = "STR"
    DEX = "DEX"
    CON = "CON"
    INT = "INT"
    WIS = "WIS"
    CHA = "CHA"
    SAVING_THROWS = "Sav. Throws"
    SKILLS = "Skills"
    WEAKNESSES_RESISTANCES_AND_IMMUNITIES = "WRI"
    SENSES = "Senses"
    LANGUAGES = "Languages"
    ADDITIONAL = "Additional"
    AVERAGE_DAMAGE = "average_damage" # needed
    ATTACK_MODIFIER = "attack_modifier" # needed
    #everything bellow defaults in the crafter as 0 or "not"
    HAS_LEGENDARY_ACTION = "has_legendary_action"
    LEGENDARY_ACTION_DAMAGE = "legendary_action_damage"
    HAS_FLIGHT = "has_flight"
    RESISTANCE_COUNT = "resistance_count"
    IMMUNITY_COUNT = "immunity_count"
    WEAKNESS_COUNT = "weakness_count"
    SAVE_DC = "save_dc"
    IS_SPELLCASTER = "is_spellcaster"
    REGENERATION_PER_ROUND = "regeneration_per_round"
    MULTIATTACK_COUNT = "multiattack_count"
    ABILITY_COUNT = "ability_count"
    ABILITY_CR_WEIGHT = "ability_cr_weight"
    RECHARGE_DAMAGE = "recharge_damage"
    LIMITED_USE_DAMAGE = "limited_use_damage"
    BONUS_ACTION_DAMAGE = "bonus_action_damage"

class SizeEnums(Enum):
    TINY = "Tiny"
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    HUGE = "Huge"
    GARGANTUAN = "Gargantuan"

class CreatureTypesEnums(Enum):
    """
    Enums which you can call on to get the DND 5e types.  \n

    this comes from the spreadsheet of course. \n

    if for some reason you wanted to add a type you would have to add it to the ENUM list.
    """
    ABERRATION = "Aberration"
    BEAST = "Beast"
    CELESTIAL = "Celestial"
    CONSTRUCT = "Construct"
    DRAGON = "Dragon"
    ELEMENTAL = "Elemental"
    FEY = "Fey"
    FIEND = "Fiend"
    FIEND_DEMON = "Fiend (Demon)"
    FIEND_DEVIL = "Fiend (Devil)"
    FIEND_DEMON_ORC = "Fiend (Demon,Orc)"
    FIEND_SHAPECHANGER = "Fiend (Shapechanger)"
    FIEND_YUGOLOTH = "Fiend (Yugoloth)"
    GIANT = "Giant"
    GIANT_GIANT_CLOUD = "Giant (Giant, Cloud)"
    GIANT_GIANT_FIRE = "Giant (Giant, Fire)"
    GIANT_GIANT_FROST = "Giant (Giant, Frost)"
    GIANT_GIANT_HILL = "Giant (Giant, Hill)"
    GIANT_GIANT_STONE = "Giant (Giant, Stone)"
    GIANT_GIANT_STORM = "Giant (Giant, Storm)"
    HUMANOID = "Humanoid"
    HUMANOID_ANY_RACE = "Humanoid (Any Race)"
    HUMANOID_DERO = "Humanoid (Derro)"
    HUMANOID_DWARF = "Humanoid (Dwarf)"
    HUMANOID_ELF = "Humanoid (Elf)"
    HUMANOID_FIRENEWT = "Humanoid (Firenewt)"
    HUMANOID_GIF = "Humanoid (Gith)"
    HUMANOID_GNOLL = "Humanoid (Gnoll)"
    HUMANOID_GOBLINOID = "Humanoid (Goblinoid)"
    HUMANOID_GRUNG = "Humanoid (Grung)"
    HUMANOID_HUMAN = "Humanoid (Human)"
    HUMANOID_KOBALD = "Humanoid (Kobold)"
    HUMANOID_MONGRELFOLK = "Humanoid (Mongrelfolk)"
    HUMANOID_NAGGA = "Humanoid (Nagpa)"
    HUMANOID_ORC = "Humanoid (Orc)"
    HUMANOID_TABAXI = "Humanoid (Tabaxi)"
    HUMANOID_TORTLE = "Humanoid (Tortle)"
    HUMANOID_TROGLODYTE = "Humanoid (Troglodyte)"
    HUMANOID_XVART = "Humanoid (Xvart)"
    HUMANOID_YUAN_TI = "Humanoid (Yuan-Ti)"
    MONSTROSITY = "Monstrosity"
    MONSTROSITY_YUAN_TI = "Monstrosity (Yuan-Ti)"
    OOZE = "Ooze"
    PLANT = "Plant"
    UNDEAD = "Undead"
    UNDEAD_TITAN = "Undead (Titan)"
    ROBOT = "Robot" #Virasco 2000 enum

class CRTypeEnums(Enum):
    """
    i've added verbal words to these. \n
    if you find these annoying you can delete them
    """
    UNKNOWN = "????"
    ZERO_NO_CHALLENGE = 0
    ONE_EIGHTH_VERY_WEAK = 1 / 8
    ONE_FORTH_WEAK = 1 / 4
    ONE_HALF_MINOR = 1 / 2
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    TWENTY = 20

class FontTypesEnums(Enum):
    FOUR_LEGENDARY_DRAGONS = "4 Legendary Dragons (★)"
    ALL_THE_LIGHTS_IN_THE_SKY_ARE_STARS = "All the Lights in the Sky Are Stars"
    ARCANE_ARTILLERY = "Arcane Artillery (☪★★★)"
    BABY_PHOENIX = "Baby Phoenix (★★★)"
    BESTIARY_OF_THE_ANCESTORS = "Bestiary of the Ancestors (★)"
    BIG_BOOK_OF_ZOMBIES = "Big Book of Zombies (?)"
    BOOK_OF_BEAUTIFUL_HORRORS = "Book of Beautiful Horrors (★★)"
    CITY_AND_WILD = "City and Wild (★★)"
    COMPENDIUM_OF_FORGOTTEN_SECRETS = "Compendium of Forgotten Secrets (☪☪★)"
    COSMIC_DRAGONS = "Cosmic Dragons (★)"
    CR_0_NIGHTMARE_FUEL = "CR 0 Nightmare Fuel (★★)"
    CURSE_OF_STRAHD = "Curse of Strahd"
    DARK_ARTS_PLAYERS_COMPANION = "Dark Arts Player's Companion (☪)"
    DARK_SUN_STAT_BLOCKS = "Dark Sun Stat Blocks (★)"
    DEMONS_SOULS_COMPENDIUM = "Demon's Souls Compendium (★)"
    DEMONS_LIST_OF_DEMONS = "Demons, Lot of Demons (★★★★)"
    DISCWORLD_UNEARTHED_ARCANA = "Discworld Unearthed Arcana (★)"
    DUNGEON_MASTERS_GUIDE = "Dungeon Master's Guide"
    ELECTRUM_DRAGONS = "Electrum Dragons (★)"
    EPIC_MONSTERS = "Epic Monsters (★)"
    FAR_REALM_BEASTS = "Far Realm Beasts (★)"
    FFXIV_COMPENDIUM = "FFXIV Compendium (★★)"
    FIGHTING_CHANCE = "Fighting Chance (r/d100)"
    FORGOTTEN_REALM_STAT_BLOCKS = "Forgotten Realms Stat Blocks (★★★)"
    GUARDIANS = "Guardians (★)"
    HANDBOOK_OF_SLIME_RHEOLOGY = "Handbook of Slime Rheology (★★)"
    HOARD_OF_THE_DRAGON_QUEEN = "Hoard of the Dragon Queen"
    FOUR_MONSTERS_BY_JACK = "https://dmdave.com/jacks-monsters-1/"
    KIRBY = "https://dmdave.com/stat-anything-kirby/"
    THANOS = "https://dmdave.com/thanos-5e-dnd/"
    CLEAR_RIVER_JELLY = "https://dreamsandfevers.blogspot.com/2018/11/clear-river-jellies.html"
    ELDER_EVILS_5E = "https://drive.google.com/file/d/1YxCrJevrMZL4M4xqCkHSQ960D7PLr2R0/view"
    VIRTUE_MOTE = "https://external-preview.redd.it/B3p2lIfLe4xsaQnEa5hLTTY52UQLm3AtRzMC2qfMajQ.jpg?auto=webp&s=94ae17d81383a0f312533bf6cba8ef6411bc1039"
    THE_SHAPE = "https://external-preview.redd.it/HNX6JWBgU5gp7BlSqtNTlUtzTPK0T4wo5RW9prNTfuI.png?auto=webp&s=345664346cc7cca7575afd996eec4b44ac640172"
    ALLUVIUM_HUNTER = "https://external-preview.redd.it/rTjZ2XDBHsf5btvFGwEb2mhD3mhy0GTmlvoGOd87shQ.jpg?auto=webp&s=a9b3be089168c52df8edec9d16bc39b5177a3343"
    ALEBRIJE = "https://homebrewery.naturalcrit.com/share/SJ-knvAt2X"
    GREED = "https://homebrewery.naturalcrit.com/share/SJbh6mfJXr"
    NECROPHAGE_AND_LEEKMIND = "https://homebrewery.naturalcrit.com/share/SJZnys8tdm"
    ASTRAL_SCOUT = "https://i.imgur.com/wikfrcy.png"
    #there are more single enemy URLS. it ends at 937
    #TODO: add single enemy URL font types.
    #starts again at row 1483
    IXORS_MANUAL_OF_MONSTROUS_FINDINGS = "Ixor's Manual of Monstrous Findings (★★)"
    MIKE_MEARLS_FIENDS = "Mike Mearls' Fiends (★)"
    MONSTER_HUNTERS_MANUAL = "Monster Hunter's Manual (★★★★)"
    MONSTER_MANUAL = "Monster Manual"
    MONSTER_MODULE = "Monster Module (★★★★)"
    MONSTER_MODULE_A_C = "Monster Module A-C"
    MORDENKAINENS_TOME_OF_FOES = "Mordenkainen's Tome of Foes"
    OUNZAIR = "Ounzair (★)"
    OUT_OF_THE_ABYSS = "Out of the Abyss"
    PATRONS_OF_THE_TALISMAN = "Patrons of the Talisman (★)"
    PLANE_SHIFT_HYRULE = "Plane Shift - Hyrule (★)"
    PRINCES_OF_THE_APOCALYPSE = "Princes of the Apocalypse"
    RENEWED_PSIONIC = "Renewed Psionic"
    RISE_OF_TIAMAT = "Rise of Tiamat"
    SINGLE_ONE_STAR = "Single (★)"
    SINGLE_DOUBLE_STAR = "Single (★★)"
    SINGLE_TRIPLE_STAR = "Single (★★★)"
    SINGLE_QUADRUPLE_STAR = "Single (★★★★)"
    SINGLE_SINGLE_OTTOMAN = "Single (☪)"
    SINGLE_DOUBLE_OTTOMAN_AND_STAR = "Single (☪☪★)"
    SKIPS_GUIDE_TO_MONSTERS = "Skip's Guide to Monsters (★★)"
    SPIDERDRAGON = "Spiderdragon (☪★)"
    SPROUTING_CHAOS_PLAYERS_COMPANION = "Sprouting Chaos Player's Companion (★★)"
    STORM_KINGS_THUNDER = "Storm King's Thunder"
    TALES_FROM_THE_YAWNING_PORTAL = "Tales from the Yawning Portal"
    THE_CUDDLE_LORD = "The Cuddle Lord (★★)"
    THE_DIANT_PRIMORDIAL_DUCK = "The Giant Primordial Duck (★)"
    THE_SOLAR_COMPENDIUM = "The Solar Compendium (★)"
    THE_TORTLE_PACKAGE = "The Tortle Package"
    THROUGH_THE_ICE_AND_SNOW = "Through the Ice and Snow (★)"
    TOMB_OF_ANNIHILATION = "Tomb of Annihilation"
    VIRASCO_2000 = "Virasco 2000"
    VOLOS_GUIDE_TO_MONSTERS = "Volo's Guide to Monsters"
    XANATHARS_GUIDE_TO_EVERYTHING = "Xanathar's Guide to Everything"
    ZOMBIE_HORDE = "Zombie Horde (★)"

class AuthorFontTypesEnums(Enum):
    FELIPEH92 = "u/FelipeH92"
    AEYANA = "u/aeyana"
    ZOWJR = "u/ZowJr"
    HELLOCHARLIEKIN = "u/hellocharliekim"
    LAMIADRAKE = "u/LamiaDrake"
    CHRISTOPHER_DORNAN = "Cristopher Dornan"
    REGEREM = "u/regerem"
    AERON_DRAKE = "u/AeronDrake"
    GENUINE_BELIEVER = "u/GenuineBelieverer"
    BLACKLIGHT85 = "u/Blacklight85"
    ZEEK0 = "u/zeek0"
    WIZARDS_OF_THE_COAST = "Wizards of the Coast"
    #there are more here
    #TODO: add author font types
    SHWIFTY_MEME_LORD = "Shwifty_meme_lord"

class AlignmentEnums(Enum):
    ANY = "ANY"
    ANY_CHAOTIC = "ANY CHAOTIC"
    ANY_EVIL = "ANY EVIL"
    ANY_GOOD = "ANY GOOD"
    ANY_NEUTRAL = "ANY NEUTRAL"
    CHAOTIC_EVIL = "CE"
    CHAOTIC_GOOD = "CG"
    CHAOTIC_NEUTRAL = "CN"
    LAWFUL_EVIL = "LE"
    LAWFUL_GOOD = "LG"
    LAWFUL_NEUTRAL = "LN"
    TRUE_NEUTRAL = "N"
    NEUTRAL_EVIL = "NE"
    NEUTRAL_GOOD = "NG"
    NOT_ALIGNED = "U"
    VARIES = "VARIES"

class SavingThrowsEnums(Enum):
    STR = "STR"
    DEX = "DEX"
    CON = "CON"
    INT = "INT"
    WIS = "WIS"
    CHA = "CHA"
    NONE = "None"

class SkillsEnums(Enum):
    ACROBATICS = "Acrobatics"
    ANIMAL_HANDLING = "Animal Handling"
    ARCANA = "Arcana"
    ATHLETICS = "Athletics"
    DECEPTION = "Deception"
    HISTORY = "History"
    INSIGHT = "Insight"
    INTIMIDATION = "Intimation"
    INVESTIGATION = "Investigation"
    MEDICINE = "Medicine"
    NATURE = "Nature"
    PERCEPTION = "Perception"
    PERFORMANCE = "Performance"
    PERSUASION = "Persuasion"
    RELIGION = "Religion"
    SLIGHT_OF_HAND = "Slight Of Hand"
    STEALTH = "Stealth"
    SURVIVAL = "Survival"
    NONE = "None"

class WRIEnums(Enum):
    """
    Weakness-es
    Resistances
    Immunities
    """
    NONE = "None"

    SLASHING_WEAKNESS = "Slashingweak"
    SLASHING_RESISTANT = "Slashingres"
    SLASHING_IMMUNE = "Slashingimmu"

    PIERCING_WEAKNESS = "Piercingweak"
    PIERCING_RESISTANT = "Piercingres"
    PIERCING_IMMUNE = "Piercingimmu"

    BLUDGEONING_WEAKNESS = "Bludgeoningweak"
    BLUDGEONING_RESISTANT = "Bludgeoningres"
    BLUDGEONING_IMMUNE = "Bludgeoningimmu"

    COLD_WEAKNESS = "Coldweak"
    COLD_RESISTANT = "Coldres"
    COLD_IMMUNE = "Coldimmu"

    POISON_WEAKNESS = "Poisonweak"
    POISON_RESISTANT = "Poisonres"
    POISON_IMMUNE = "Poisonimmu"

    ACID_WEAKNESS = "Acidweak"
    ACID_RESISTANT = "Acidres"
    ACID_IMMUNE = "Acidimmu"

    PSYCHIC_WEAKNESS = "Psychicweak"
    PSYCHIC_RESISTANT = "Psychicres"
    PSYCHIC_IMMUNE = "Psychicimmu"

    FIRE_WEAKNESS = "Fireweak"
    FIRE_RESISTANT = "Fireres"
    FIRE_IMMUNE = "Fireimmu"

    NECROTIC_WEAKNESS = "Necroticweak"
    NECROTIC_RESISTANT = "Necroticres"
    NECROTIC_IMMUNE = "Necroticimmu"

    RADIANT_WEAKNESS = "Radiantweak"
    RADIANT_RESISTANT = "Radiantres"
    RADIANT_IMMUNE = "Radiantimmu"

    FORCE_WEAKNESS = "Forceweak"
    FORCE_RESISTANT = "Forceres"
    FORCE_IMMUNE = "Forceimmu"

    THUNDER_WEAKNESS = "Thunderweak"
    THUNDER_RESISTANT = "Thunderres"
    THUNDER_IMMUNE = "Thunderimmu"

    LIGHTNING_WEAKNESS = "Lightningweak"
    LIGHTNING_RESISTANT = "Lightningres"
    LIGHTNING_IMMUNE = "Lightningimmu"

class SensesEnums(Enum):
    NORMAL = "Normal"
    NONE = "None"
    DARKVISION_SIXTY = "Darkvision 60"
    BLINDSIGHT_THIRTY = "Blindsight 30"
    BLINDSIGHT_ONE_TWENTY = "Blindsight 120"
    TREMORSENSE_THIRTY = "Tremorsesen 30"
    TRUSIGHT_ONE_TWENTY = "Trusight 120"
    #TODO: add the rest of these senses

class LanguagesEnums(Enum):
    """
    got from here:
    https://www.reddit.com/r/DnD/comments/ejs4yu/languages/
    """
    NONE = "None"

    #Standard languages
    COMMON = "Common"
    DWARVISH = "Dwarvish"
    ELVISH = "Elvish"
    GIANT = "Giant"
    GNOMISH = "Gnomish"
    GOBLIN = "Goblin"
    HALFLING = "Halfling"
    ORC = "Orc"

    #Exotic language
    ABYSSAL = "Abyssal"
    CELESTIAL = "Celestial"
    DRACONIC = "Draconic"
    DEEP_SPEECH = "Deep Speech"
    INFERNAL = "Infernal"
    PRIMODIAL_AQUAN = "Primodial Aquan"
    PRIMODIAL_ARUAN = "Primodial Aruan"
    PRIMODIAL_IGNAN = "Primodial Ignan"
    PRIMODIAL_TERRAN = "Primodial Terran"
    SYLVAN = "Sylvan"
    UNDERCOMMON = "Undercommon"
    THIEVES_CANT = "Thieves Cant"

class ConditionEnums(Enum):
    """
    https://www.dndbeyond.com/sources/dnd/basic-rules-2014/appendix-a-conditions
    """
    BLINDED = "Blinded",
    CHARMED = "Charmed",
    DEAFENED = "Deafened",
    EXHAUSTION = "Exhaustion",
    FRIGHTENED = "Frightened",
    GRAPPLED = "Grappled",
    INCAPACITATED = "Incapacitated",
    INVISIBLE = "Invisible",
    PARALYZED = "Paralyzed",
    PETRIFIED = "Petrified",
    POISONED = "Poisoned",
    PRONE = "Prone",
    RESTRAINED = "Restrained",
    STUNNED = "Stunned",
    UNCONSCIOUS = "Unconscious",