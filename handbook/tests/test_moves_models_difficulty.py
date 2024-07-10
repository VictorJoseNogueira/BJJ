from .test_move_base import MovesTestBase
from django.core.exceptions import ValidationError


class DifficultyModelTest(MovesTestBase):
    def setUp(self) -> None:
        self.difficulty = self.make_difficulty(
            difficulty='Difficulty test'
        )
        return super().setUp()

    def test_move_difficulty_model_string_represantation(self):
        self.assertEqual(
            str(self.difficulty),
            self.difficulty.difficulty
            )

    def test_move_difficulty_model_max_length_is_65_chars(self):
        self.difficulty.difficulty = 'A' * 66
        with self.assertRaises(ValidationError):
            self.difficulty.full_clean()
