from django.test import TestCase
from django.urls import reverse


class Move_URL_test(TestCase):
    def test_handbook_home_url_is_correct(self):
        url = reverse("moves:home")
        self.assertEqual(url, '/')

    def test_handbook_move_url_is_correct(self):
        url = reverse("moves:move", kwargs={'movement_id': 2})
        self.assertEqual(url, '/moves/2/')

    def test_handbook_difficulty_url_is_correct(self):
        url = reverse("moves:difficulty", kwargs={'difficulty_id': 2})
        self.assertEqual(url, '/moves/dificuldades/2/')

    def test_handbook_category_url_is_correct(self):
        url = reverse("moves:category", kwargs={'category_id': 1})
        self.assertEqual(url, '/moves/categorias/1/')
