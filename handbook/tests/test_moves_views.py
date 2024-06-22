from django.test import TestCase
from django.urls import reverse, resolve
from handbook import views


class Moves_views_test(TestCase):

    # home
    def test_move_home_view_return_status_code_200_ok(self):
        response = self.client.get(reverse("moves:home"))
        self.assertEqual(response.status_code, 200)

    def test_move_home_view_loads_correct_template(self):
        response = self.client.get(reverse("moves:home"))
        self.assertTemplateUsed(response, "handbook/pages/index.html")

    def test_move_home_shows_no_movements_found_if_no_movements(self):
        response = self.client.get(reverse("moves:home"))
        self.assertIn('Administrador esta preguiçoso mande ele aprovar as tecnicas logo', response.content.decode('utf-8'))  # noqa E501

    def test_move_home_view_funcion_is_correct(self):
        view = resolve(reverse("moves:home"))
        self.assertIs(view.func, views.home)

    # category
    def test_move_category_view_funcion_is_correct(self):
        view = resolve(reverse("moves:category", kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category_def)

    # difficulty
    def test_move_difficulty_view_funcion_is_correct(self):
        view = resolve(reverse("moves:difficulty", kwargs={'difficulty_id': 2}))  # noqa R501
        self.assertIs(view.func, views.difficulty_def)

# details

    def test_move_details_view_funcion_is_correct(self):
        view = resolve(reverse("moves:move", kwargs={'movement_id': 2}))
        self.assertIs(view.func, views.move)



'''    def test_move_category_view_return_status_code_200_ok(self):
        response = self.client.get(reverse("moves:category"))
        self.assertEqual(response.status_code, 200)

    def test_move_category_view_loads_correct_template(self):
        response = self.client.get(reverse("moves:category"))
        self.assertTemplateUsed(response, "handbook/pages/category.html")

    def test_move_difficulty_view_return_status_code_200_ok(self):
        response = self.client.get(reverse("moves:difficulty"))
        self.assertEqual(response.status_code, 200)

    def test_move_difficulty_view_loads_correct_template(self):
        response = self.client.get(reverse("moves:difficulty"))
        self.assertTemplateUsed(response, "handbook/pages/index.html")

    def test_move_details_view_return_status_code_200_ok(self):
        response = self.client.get(reverse("moves:move"))
        self.assertEqual(response.status_code, 200)

    def test_move_details_view_loads_correct_template(self):
        response = self.client.get(reverse("moves:move"))
        self.assertTemplateUsed(response, "handbook/pages/index.html")
''' # noqa E501
