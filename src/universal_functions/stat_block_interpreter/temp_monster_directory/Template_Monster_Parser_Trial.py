from universal_functions.enums import spreadsheet_enums

template_monster_parser_trial_monster_dict = \
    {
        spreadsheet_enums.SpreadsheetKeysEnums.NAME.value :
            'Template Monster, Parser Trial',
        spreadsheet_enums.SpreadsheetKeysEnums.SIZE.value :
            spreadsheet_enums.SizeEnums.SMALL.value,
        spreadsheet_enums.SpreadsheetKeysEnums.TYPE.value :
            spreadsheet_enums.CreatureTypesEnums.CONSTRUCT.value,
        spreadsheet_enums.SpreadsheetKeysEnums.CR.value :
            0.5,
        spreadsheet_enums.SpreadsheetKeysEnums.URL.value :
            'https://example.com/stat-block',
        spreadsheet_enums.SpreadsheetKeysEnums.FONT.value :
            'DND_5E_CR_versus_player_calculator',
        spreadsheet_enums.SpreadsheetKeysEnums.AUTHOR.value :
            'Codex',
        spreadsheet_enums.SpreadsheetKeysEnums.HP.value :
            13,
        spreadsheet_enums.SpreadsheetKeysEnums.AC.value :
            12,
        spreadsheet_enums.SpreadsheetKeysEnums.SPEEDS.value :
            '30, climb 20',
        spreadsheet_enums.SpreadsheetKeysEnums.ALIGN.value :
            'almost chaos',
        spreadsheet_enums.SpreadsheetKeysEnums.STR.value :
            8,
        spreadsheet_enums.SpreadsheetKeysEnums.DEX.value :
            14,
        spreadsheet_enums.SpreadsheetKeysEnums.CON.value :
            10,
        spreadsheet_enums.SpreadsheetKeysEnums.INT.value :
            6,
        spreadsheet_enums.SpreadsheetKeysEnums.WIS.value :
            9,
        spreadsheet_enums.SpreadsheetKeysEnums.CHA.value :
            4,
        spreadsheet_enums.SpreadsheetKeysEnums.SAVING_THROWS.value :
            ", ".join([spreadsheet_enums.SavingThrowsEnums.STR.value, spreadsheet_enums.SavingThrowsEnums.DEX.value]),
        spreadsheet_enums.SpreadsheetKeysEnums.SKILLS.value :
            ", ".join([spreadsheet_enums.SkillsEnums.STEALTH.value, spreadsheet_enums.SkillsEnums.HISTORY.value]),
        spreadsheet_enums.SpreadsheetKeysEnums.WEAKNESSES_RESISTANCES_AND_IMMUNITIES.value :
            ", ".join([spreadsheet_enums.WRIEnums.RADIANT_WEAKNESS.value, spreadsheet_enums.WRIEnums.FIRE_RESISTANT.value, spreadsheet_enums.WRIEnums.NECROTIC_RESISTANT.value, spreadsheet_enums.WRIEnums.POISON_IMMUNE.value]),
        spreadsheet_enums.SpreadsheetKeysEnums.SENSES.value :
            spreadsheet_enums.SensesEnums.DARKVISION_SIXTY.value,
        spreadsheet_enums.SpreadsheetKeysEnums.LANGUAGES.value :
            spreadsheet_enums.LanguagesEnums.COMMON.value,
        spreadsheet_enums.SpreadsheetKeysEnums.ADDITIONAL.value :
            'None',
        spreadsheet_enums.SpreadsheetKeysEnums.AVERAGE_DAMAGE.value :
            5.5,
        spreadsheet_enums.SpreadsheetKeysEnums.ATTACK_MODIFIER.value :
            4,
        spreadsheet_enums.SpreadsheetKeysEnums.HAS_LEGENDARY_ACTION.value :
            False,
        spreadsheet_enums.SpreadsheetKeysEnums.LEGENDARY_ACTION_DAMAGE.value :
            0,
        spreadsheet_enums.SpreadsheetKeysEnums.HAS_FLIGHT.value :
            False,
        spreadsheet_enums.SpreadsheetKeysEnums.RESISTANCE_COUNT.value :
            2,
        spreadsheet_enums.SpreadsheetKeysEnums.IMMUNITY_COUNT.value :
            1,
        spreadsheet_enums.SpreadsheetKeysEnums.WEAKNESS_COUNT.value :
            1,
        spreadsheet_enums.SpreadsheetKeysEnums.SAVE_DC.value :
            11,
        spreadsheet_enums.SpreadsheetKeysEnums.IS_SPELLCASTER.value :
            False,
        spreadsheet_enums.SpreadsheetKeysEnums.REGENERATION_PER_ROUND.value :
            0,
        spreadsheet_enums.SpreadsheetKeysEnums.MULTIATTACK_COUNT.value :
            0,
        spreadsheet_enums.SpreadsheetKeysEnums.ABILITY_COUNT.value :
            1,
        spreadsheet_enums.SpreadsheetKeysEnums.ABILITY_CR_WEIGHT.value :
            2,
        spreadsheet_enums.SpreadsheetKeysEnums.RECHARGE_DAMAGE.value :
            0,
        spreadsheet_enums.SpreadsheetKeysEnums.LIMITED_USE_DAMAGE.value :
            6,
        spreadsheet_enums.SpreadsheetKeysEnums.BONUS_ACTION_DAMAGE.value :
            1,
        "actions" :
            [
                {
                    'name': 'action \\- test spark',
                    'action_type': 'action',
                    'attack_type': 'ranged_spell_attack',
                    'hit_modifier': 4,
                    'damage': '1d6 + 2',
                    'damage_type': 'fire',
                    'range': 60,
                    'notes': 'Link in the action name should become plain text.'
                 },
                {
                    'name': 'action \\- bad math shove',
                    'action_type': 'bonus_action',
                    'attack_type': 'saving_throw',
                    'save_dc': 11,
                    'save_stat': 'str',
                    'damage': '1d4 \\- 1',
                    'damage_type': 'bludgeoning',
                    'range': 5,
                    'notes': 'Negative constants should not scare the parser.'
                 }
            ],
    }
