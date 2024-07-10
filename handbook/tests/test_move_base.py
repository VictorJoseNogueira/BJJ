from django.test import TestCase
from handbook.models import Category, Difficulty, Moves
from django.contrib.auth.models import User


class MovesTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_category(self, category=''):
        return Category.objects.create(category=category)

    def make_author(self, first_name='user', last_name='name', username='username', password='321', email='username@email.com'):  # noqa E501
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email)

    def make_difficulty(self, difficulty='DIFICULDADE'):
        return Difficulty.objects.create(difficulty=difficulty)

    def make_moviment(self,
                      category_data=None,
                      difficulty_data=None,
                      author_data=None,
                      title='Movement title',
                      title_slug='movement-title',
                      is_published=True,
                      Video_link='https://www.youtube.com/watch?v=WXa6eScLJxE'):  # noqa E501  
        if category_data is None:
            category_data = {}
        if difficulty_data is None:
            difficulty_data = {}
        if author_data is None:
            author_data = {}

        return Moves.objects.create(
            category=self.make_category(**category_data),
            difficulty=self.make_difficulty(**difficulty_data),
            author=self.make_author(**author_data),
            title=title,
            title_slug=title_slug,
            Video_link=Video_link,
            is_published=is_published)  # noqa E501