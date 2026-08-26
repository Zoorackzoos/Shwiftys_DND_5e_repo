# for the love of your life.
from src.universal_functions.craft_cr_from_monster_stat_block import plug_monster_var_values_into_get_cr_from_monster
from src.universal_functions.get_average_damage import get_average_damage
from src.universal_functions.spreadsheet_stuff.spreadsheet_updaters.update_homebrew_monster_spreadsheet import \
    update_homebrew_monster_spreadsheet
from universal_functions.vars.enums import spreadsheet_enums
from src.universal_functions.vars.get_stringified_list_of_enums import get_stringified_list_of_enums

calculus_monster_derivative_monster_dict = \
    {
        spreadsheet_enums.SpreadsheetKeysEnums.NAME.value :
            "Calculus Monster, Derivative",
        spreadsheet_enums.SpreadsheetKeysEnums.SIZE.value :
            spreadsheet_enums.SizeEnums.MEDIUM.value,
        spreadsheet_enums.SpreadsheetKeysEnums.TYPE.value :
            spreadsheet_enums.CreatureTypesEnums.MONSTROSITY.value,
        spreadsheet_enums.SpreadsheetKeysEnums.CR.value :
            spreadsheet_enums.CRTypeEnums.THREE.value, # update this later in the updater file or here
        spreadsheet_enums.SpreadsheetKeysEnums.URL.value :
            "https://docs.google.com/document/d/1evELbjfqqUkLtBtvN27-di9otjVPgX5iiDu2qsMbo70/edit?tab=t.0",
        spreadsheet_enums.SpreadsheetKeysEnums.FONT.value :
            spreadsheet_enums.FontTypesEnums.VIRASCO_2000.value,
        spreadsheet_enums.SpreadsheetKeysEnums.AUTHOR.value :
            spreadsheet_enums.AuthorFontTypesEnums.SHWIFTY_MEME_LORD.value,
        spreadsheet_enums.SpreadsheetKeysEnums.HP.value :
            80,
        spreadsheet_enums.SpreadsheetKeysEnums.AC.value :
            15,
        spreadsheet_enums.SpreadsheetKeysEnums.SPEEDS.value :
            60,
        spreadsheet_enums.SpreadsheetKeysEnums.ALIGN.value :
            spreadsheet_enums.AlignmentEnums.CHAOTIC_EVIL.value,
        spreadsheet_enums.SpreadsheetKeysEnums.STR.value :
            16,
        spreadsheet_enums.SpreadsheetKeysEnums.DEX.value :
            18,
        spreadsheet_enums.SpreadsheetKeysEnums.CON.value :
            18,
        spreadsheet_enums.SpreadsheetKeysEnums.INT.value :
            20,
        spreadsheet_enums.SpreadsheetKeysEnums.WIS.value :
            20,
        spreadsheet_enums.SpreadsheetKeysEnums.CHA.value :
            14,
        spreadsheet_enums.SpreadsheetKeysEnums.SAVING_THROWS.value :
            get_stringified_list_of_enums(
                list_of_enums=
                [
                    spreadsheet_enums.SavingThrowsEnums.STR,
                    spreadsheet_enums.SavingThrowsEnums.INT,
                    spreadsheet_enums.SavingThrowsEnums.WIS,
                    spreadsheet_enums.SavingThrowsEnums.DEX
                ]
            ),
        spreadsheet_enums.SpreadsheetKeysEnums.SKILLS.value :
            spreadsheet_enums.SkillsEnums.HISTORY.value,
        spreadsheet_enums.SpreadsheetKeysEnums.WEAKNESSES_RESISTANCES_AND_IMMUNITIES.value :
            get_stringified_list_of_enums(
                list_of_enums=
                [
                    spreadsheet_enums.WRIEnums.PSYCHIC_IMMUNE.value,
                    spreadsheet_enums.WRIEnums.NECROTIC_RESISTANT.value,
                    spreadsheet_enums.WRIEnums.ACID_IMMUNE.value
                ]
            ),
        spreadsheet_enums.SpreadsheetKeysEnums.SENSES :
            spreadsheet_enums.SensesEnums.NORMAL.value,
        spreadsheet_enums.SpreadsheetKeysEnums.LANGUAGES.value :
            spreadsheet_enums.LanguagesEnums.NONE.value,
        spreadsheet_enums.SpreadsheetKeysEnums.ADDITIONAL.value :
            "None",
        spreadsheet_enums.SpreadsheetKeysEnums.AVERAGE_DAMAGE.value :
            get_average_damage
            (
                dice_dict=
                {
                    4: 0,
                    6: 0,
                    8: 1,
                    12: 0,
                    20: 0,
                    "constant": 2
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
            1,
        spreadsheet_enums.SpreadsheetKeysEnums.IMMUNITY_COUNT.value :
            2,
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

def get_and_print_out_derivative_cr_out(tab_amount="\t"):
    calculus_monster_cr = \
        (plug_monster_var_values_into_get_cr_from_monster
            (
            monster_var=calculus_monster_derivative_monster_dict,
            tab_amount=tab_amount
        )
        )
    print("calculus_monster_cr =", calculus_monster_cr)

if __name__ == "__main__":
    tab_amount = "\t"
    #get_and_print_out_derivative_cr_out(tab_amount=tab_amount)
    update_homebrew_monster_spreadsheet(
        monster_dict=calculus_monster_derivative_monster_dict,
        path_to_monsters_csv_file="../../../../../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv",
        tab_amount=tab_amount
    )