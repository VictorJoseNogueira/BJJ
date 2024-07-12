from django.urls import resolve, reverse

from handbook import views

from .test_move_base import MovesTestBase

# teste @skip("texto")
# self.fail('texto')


class Moves_views_test(MovesTestBase):
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

    def test_move_detail_dont_load_movement_not_published(self):
        """ teste movement is_published False dont Show"""
        # need movement
        move = self.make_moviment(is_published=False)
        response = self.client.get(reverse("moves:move", kwargs={'movement_id': move.movement_id},))  # noqa E501
        self.assertEqual(response.status_code, 404)
