from django.urls import resolve, reverse

from handbook import views

from .test_move_base import MovesTestBase

# teste @skip("texto")
# self.fail('texto')


class Moves_category_views_test(MovesTestBase):
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

    def test_move_category_dont_load_movements_not_published(self):
        """ teste movement is_published False dont Show"""
        # need movement
        move = self.make_moviment(is_published=False)
        response = self.client.get(reverse("moves:category", kwargs={'category_id': move.category.id},))  # noqa E501
        self.assertEqual(response.status_code, 404)
