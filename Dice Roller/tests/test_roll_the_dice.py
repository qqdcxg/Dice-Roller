import tkinter as tk
import unittest

import roll_the_dice_ui
from roll_the_dice import get_die_face_name, get_die_face_positions, roll_single_die


class DiceRollTests(unittest.TestCase):
    def test_roll_single_die_returns_valid_face(self):
        value = roll_single_die()
        self.assertIn(value, range(1, 7))

    def test_die_face_positions_have_expected_shape(self):
        face_name = get_die_face_name(4)
        positions = get_die_face_positions(4)
        self.assertEqual(face_name, "die_4")
        self.assertEqual(len(positions), 4)

    def test_input_box_and_button_do_not_overlap_preview(self):
        root = tk.Tk()
        root.withdraw()
        try:
            roll_the_dice_ui.build_ui(root)
            self.assertEqual(roll_the_dice_ui.entry_times.grid_info()["column"], 0)
            self.assertEqual(roll_the_dice_ui.button_roll.grid_info()["column"], 0)
            self.assertEqual(roll_the_dice_ui.button_roll.grid_info()["row"], 4)
            self.assertEqual(roll_the_dice_ui.entry_times.grid_info()["row"], 3)
        finally:
            root.destroy()


if __name__ == "__main__":
    unittest.main()
