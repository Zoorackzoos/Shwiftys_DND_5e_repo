# for the love of your life.
from src.universal_functions.get_average_damage import get_average_damage
from universal_functions.enums import spreadsheet_enums
from src.universal_functions.vars.get_stringified_list_of_enums import get_stringified_list_of_enums


# please use mr. intro_purple here as a default for every monster dict here on out
intro_purple_foot_clan_ninja_monster_dict = \
    {
        spreadsheet_enums.SpreadsheetKeysEnums.NAME.value :
            "intro purple foot clan ninja",
        spreadsheet_enums.SpreadsheetKeysEnums.SIZE.value :
            spreadsheet_enums.SizeEnums.MEDIUM.value,
        spreadsheet_enums.SpreadsheetKeysEnums.TYPE.value :
            spreadsheet_enums.CreatureTypesEnums.HUMANOID.value,
        spreadsheet_enums.SpreadsheetKeysEnums.CR.value :
            spreadsheet_enums.CRTypeEnums.ONE_FORTH_WEAK.value,
        spreadsheet_enums.SpreadsheetKeysEnums.URL.value :
            "https://docs.google.com/document/d/1JUiihzhgPS4Rg1ofP1xjbswx8sFso69X1KWdyWuTT78/edit?tab=t.0",
        spreadsheet_enums.SpreadsheetKeysEnums.FONT.value :
            spreadsheet_enums.FontTypesEnums.VIRASCO_2000.value,
        spreadsheet_enums.SpreadsheetKeysEnums.AUTHOR.value :
            spreadsheet_enums.AuthorFontTypesEnums.SHWIFTY_MEME_LORD.value,
        spreadsheet_enums.SpreadsheetKeysEnums.HP.value :
            20,
        spreadsheet_enums.SpreadsheetKeysEnums.AC.value :
            12,
        spreadsheet_enums.SpreadsheetKeysEnums.SPEEDS.value :
            30,
        spreadsheet_enums.SpreadsheetKeysEnums.ALIGN.value :
            spreadsheet_enums.AlignmentEnums.NEUTRAL_EVIL.value,
        spreadsheet_enums.SpreadsheetKeysEnums.STR.value :
            10,
        spreadsheet_enums.SpreadsheetKeysEnums.DEX.value :
            12,
        spreadsheet_enums.SpreadsheetKeysEnums.CON.value :
            12,
        spreadsheet_enums.SpreadsheetKeysEnums.INT.value :
            10,
        spreadsheet_enums.SpreadsheetKeysEnums.WIS.value :
            10,
        spreadsheet_enums.SpreadsheetKeysEnums.CHA.value :
            10,
        spreadsheet_enums.SpreadsheetKeysEnums.SAVING_THROWS.value :
            spreadsheet_enums.SavingThrowsEnums.NONE.value,
        spreadsheet_enums.SpreadsheetKeysEnums.SKILLS.value :
            spreadsheet_enums.SkillsEnums.NONE.value,
        spreadsheet_enums.SpreadsheetKeysEnums.WEAKNESSES_RESISTANCES_AND_IMMUNITIES.value :
            spreadsheet_enums.WRIEnums.NONE,
        spreadsheet_enums.SpreadsheetKeysEnums.SENSES :
            spreadsheet_enums.SensesEnums.NORMAL.value,
        spreadsheet_enums.SpreadsheetKeysEnums.LANGUAGES.value :
            get_stringified_list_of_enums
            (
                list_of_enums=[spreadsheet_enums.LanguagesEnums.COMMON.value,
                               spreadsheet_enums.LanguagesEnums.THIEVES_CANT.value]
            ),
        spreadsheet_enums.SpreadsheetKeysEnums.ADDITIONAL.value :
            "None",
        spreadsheet_enums.SpreadsheetKeysEnums.AVERAGE_DAMAGE.value :
            get_average_damage
            (
                dice_dict=
                {
                    6 : 1,
                    "constant" : 2
                }
            ),
        spreadsheet_enums.SpreadsheetKeysEnums.ATTACK_MODIFIER.value :
            3,
        spreadsheet_enums.SpreadsheetKeysEnums.HAS_LEGENDARY_ACTION.value :
            False,
        spreadsheet_enums.SpreadsheetKeysEnums.LEGENDARY_ACTION_DAMAGE.value :
            0,
        spreadsheet_enums.SpreadsheetKeysEnums.HAS_FLIGHT.value :
            False,
        spreadsheet_enums.SpreadsheetKeysEnums.RESISTANCE_COUNT.value :
            0,
        spreadsheet_enums.SpreadsheetKeysEnums.IMMUNITY_COUNT.value :
            0,
        spreadsheet_enums.SpreadsheetKeysEnums.WEAKNESS_COUNT.value :
            0,
        spreadsheet_enums.SpreadsheetKeysEnums.SAVE_DC.value :
            0,
        spreadsheet_enums.SpreadsheetKeysEnums.IS_SPELLCASTER.value :
            False,
        spreadsheet_enums.SpreadsheetKeysEnums.REGENERATION_PER_ROUND.value :
            0,
        spreadsheet_enums.SpreadsheetKeysEnums.MULTIATTACK_COUNT.value :
            0,
        spreadsheet_enums.SpreadsheetKeysEnums.ABILITY_COUNT.value :
            0,
        spreadsheet_enums.SpreadsheetKeysEnums.ABILITY_CR_WEIGHT.value :
            0,
        spreadsheet_enums.SpreadsheetKeysEnums.RECHARGE_DAMAGE.value :
            0,
        spreadsheet_enums.SpreadsheetKeysEnums.LIMITED_USE_DAMAGE.value :
            0,
        spreadsheet_enums.SpreadsheetKeysEnums.BONUS_ACTION_DAMAGE.value :
            0,
    }