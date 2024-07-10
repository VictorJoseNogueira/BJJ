from .test_move_base import MovesTestBase, Moves
from django.core.exceptions import ValidationError
from parameterized import parameterized  # type: ignore


class MovesModelTest(MovesTestBase):
    def setUp(self) -> None:
        self.movement = self.make_moviment()
        return super().setUp()

    @parameterized.expand([
            ('title', 120),
            ('title', 120)
        ])
    def test_movement_filds_max_length(self, fild, max_length):
        setattr(self.movement, fild, "A" * (max_length+1))
        with self.assertRaises(ValidationError):
            self.movement.full_clean()  # aqui a validação ocorre

    def test_movement_is_published_is_False_by_default(self):
        moves = Moves(
                      category=self.make_category(category='test default category'),  # noqa E501
                      difficulty=self.make_difficulty(difficulty='test default difficulty'),  # noqa E501
                      author=self.make_author(username='ze'),
                      title='Movement title',
                      title_slug='movement-title',
                      Video_link='https://www.youtube.com/watch?v=WXa6eScLJxE')  # noqa E501
        print(moves)
        moves.full_clean()
        moves.save()
        self.assertFalse(moves.is_published)

    def test_movement_string_representation(self):
        self.movement.title = 'testing representation'  # noqa E501
        self.movement.full_clean()
        self.movement.save()
        self.assertEqual(
            str(self.movement),
            'testing representation',
            msg='Movement string needs to be the same as title'
        )
