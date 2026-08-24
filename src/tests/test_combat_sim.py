import unittest
from unittest.mock import patch

from A_GUI_programs.combat_sim.get_damage_and_get_chance_to_hit import get_chance_to_hit


class TestCombatSim(unittest.TestCase):
    def test_get_chance_to_hit_adds_hit_modifier_to_d20_roll(self):
        with patch("src.combat_sim.combat_sim.random.randint", return_value=12):
            self.assertEqual(
                17,
                get_chance_to_hit(hit_modifier=5)
            )

    def test_get_chance_to_hit_adds_negative_hit_modifier_to_d20_roll(self):
        with patch("src.combat_sim.combat_sim.random.randint", return_value=8):
            self.assertEqual(
                6,
                get_chance_to_hit(hit_modifier=-2)
            )

    def test_get_damage_adds_all_damage_dice_rolls(self):
        damage_dice = {
            6: 2,
            4: 1,
            "constant": 0
        }

        with patch("src.combat_sim.combat_sim.random.randint", side_effect=[3, 5, 2]):
            self.assertEqual(
                10,
                get_damage(damage_dice=damage_dice)
            )

    def test_get_damage_adds_constant_damage_modifier(self):
        damage_dice = {
            6: 1,
            "constant": 2
        }

        with patch("src.combat_sim.combat_sim.random.randint", return_value=4):
            self.assertEqual(
                6,
                get_damage(damage_dice=damage_dice)
            )

    def test_get_damage_adds_negative_constant_damage_modifier(self):
        damage_dice = {
            4: 1,
            "constant": -1
        }

        with patch("src.combat_sim.combat_sim.random.randint", return_value=3):
            self.assertEqual(
                2,
                get_damage(damage_dice=damage_dice)
            )


if __name__ == "__main__":
    unittest.main()
