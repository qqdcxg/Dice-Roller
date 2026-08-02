import unittest

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


if __name__ == "__main__":
    unittest.main()
