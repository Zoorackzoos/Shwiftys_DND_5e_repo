import unittest
from unittest.mock import patch

from src.A_GUI_programs.combat_sim.combat_sim_cycle_combat import (
    get_attack_result_lines,
    get_damage_dice_from_damage_string,
    get_monster_actions,
)


class TestCombatSimCycleCombatAttacks(unittest.TestCase):
    def test_get_damage_dice_from_damage_string_handles_constant_damage(self):
        self.assertEqual(
            {
                20: 0,
                12: 0,
                10: 0,
                8: 0,
                6: 1,
                4: 0,
                "constant": 2
            },
            get_damage_dice_from_damage_string("1d6 + 2")
        )

    def test_get_damage_dice_from_damage_string_handles_negative_constant_damage(self):
        self.assertEqual(
            -1,
            get_damage_dice_from_damage_string("1d4 - 1")["constant"]
        )

    def test_get_monster_actions_defaults_to_empty_list(self):
        self.assertEqual(
            [],
            get_monster_actions(monster_dict={})
        )

    def test_get_attack_result_lines_rolls_martial_attack(self):
        action = {
            "attack_type": "melee_attack",
            "hit_modifier": 4,
            "damage": "1d6 + 2"
        }

        with patch(
                "src.A_GUI_programs.combat_sim.get_damage_and_get_chance_to_hit.random.randint",
                side_effect=[10, 6]
        ):
            self.assertEqual(
                [
                    "chance_to_hit = 14",
                    "damage = 8"
                ],
                get_attack_result_lines(action=action)
            )

    def test_get_attack_result_lines_displays_saving_throw_attack(self):
        action = {
            "attack_type": "saving_throw",
            "save_stat": "dex",
            "save_dc": 14,
            "damage": "2d8 + 3"
        }

        self.assertEqual(
            [
                "save_stat = dex",
                "save_dc = 14",
                "damage = 2d8 + 3"
            ],
            get_attack_result_lines(action=action)
        )

    def test_get_attack_result_lines_rejects_non_attack_action(self):
        action = {
            "attack_type": "utility",
            "name": "smoke bomb"
        }

        self.assertEqual(
            ["this type of action is not a attack"],
            get_attack_result_lines(action=action)
        )


if __name__ == "__main__":
    unittest.main()
