from .test_move_base import MovesTestBase
from django.core.exceptions import ValidationError


class CategoryModelTest(MovesTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(
            category='category test'
        )
        return super().setUp()

    def test_move_category_model_string_represantation(self):
        self.assertEqual(
            str(self.category),
            self.category.category
            )

    def test_move_category_model_max_length_is_65_chars(self):
        self.category.category = 'A' * 70
        with self.assertRaises(ValidationError):
            self.category.full_clean()
