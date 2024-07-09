from django.urls import reverse, resolve
from handbook import views
from .test_move_base import MovesTestBase

# teste @skip("texto")
# self.fail('texto')


class Moves_views_test(MovesTestBase):
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

    def test_moves_home_template_load_movements(self):
        self.make_moviment()
        response = self.client.get(reverse("moves:home"))
        content = response.content.decode('utf-8')
        response_context_movement = response.context['moves']
        self.assertIn('DIFICULDADE', content)
        self.assertNotIn('username', content)
        self.assertEqual(len(response_context_movement), 1)

    # category
    def test_move_category_view_funcion_is_correct(self):
        view = resolve(reverse("moves:category", kwargs={'category_id': 1000}))
        self.assertIs(view.func, views.category_def)

    def test_move_category_view_return_404_if_no_moves_found(self):
        response = self.client.get(reverse("moves:category", kwargs={'category_id': 1000}))  # noqa E501
        self.assertEqual(response.status_code, 404)

    def test_moves_category_template_loads_movements(self):
        needed_tittle = "this is a category test"
        # create a move
        self.make_moviment(title=needed_tittle)

        response = self.client.get(reverse("moves:category", kwargs={'category_id': 1},))  # noqa E501
        content = response.content.decode("utf-8")
        response_context_movements = response.context['moves']  # noqa
        # check if one move exist
        self.assertIn(needed_tittle, content)
        ...

    # difficulty
    def test_move_difficulty_view_funcion_is_correct(self):
        view = resolve(reverse("moves:difficulty", kwargs={'difficulty_id': 2}))  # noqa E501
        self.assertIs(view.func, views.difficulty_def)

    def test_move_difficulty_view_return_404_if_no_moves_found(self):
        response = self.client.get(reverse("moves:difficulty", kwargs={'difficulty_id': 1000}))  # noqa E501
        self.assertEqual(response.status_code, 404)

    def test_moves_difficulty_template_loads_movements(self):
        needed_tittle = "this is a difficulty test"
        # create a move
        self.make_moviment(title=needed_tittle)

        response = self.client.get(reverse("moves:difficulty", kwargs={'difficulty_id': 1},))  # noqa E501
        content = response.content.decode("utf-8")
        response_context_movements = response.context['moves']  # noqa
        # check if one move exist
        self.assertIn(needed_tittle, content)

    # details
    def test_move_details_view_funcion_is_correct(self):
        view = resolve(reverse("moves:move", kwargs={'movement_id': 2}))
        self.assertIs(view.func, views.move)

    def test_move_details_view_return_404_if_no_moves_found(self):
        response = self.client.get(reverse("moves:move", kwargs={'movement_id': 1000}))  # noqa E501
        self.assertEqual(response.status_code, 404)

    def test_moves_detail_template_loads_the_correct_movement(self):
        needed_tittle = "this is a detail page - it load one move"

        # create a move
        self.make_moviment(title=needed_tittle)

        response = self.client.get(reverse("moves:move", kwargs={'movement_id': 1},))  # noqa E501
        content = response.content.decode("utf-8")
        # check if one move exist
        self.assertIn(needed_tittle, content)
