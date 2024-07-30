from django.urls import resolve, reverse

from handbook import views
from unittest.mock import patch
from .test_move_base import MovesTestBase

# teste @skip("texto")
# self.fail('texto')


class Moves_difficulty_views_test(MovesTestBase):
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

    def test_move_difficulty_dont_load_movements_not_published(self):
        """ teste movement is_published False dont Show"""
        # need movement
        move = self.make_moviment(is_published=False)
        response = self.client.get(reverse("moves:difficulty", kwargs={'difficulty_id': move.difficulty.id},))  # noqa E501
        self.assertEqual(response.status_code, 404)

    @patch('handbook.views.PER_PAGE', new=3)
    def test_move_difficulty_is_paginated(self):

        for i in range(8):
            kwargs = {'title_slug': f'r{i}', 'author_data': {'username': f'ú{i}'},  'difficulty_data': {'difficulty': 'Dificuldade'},}  # noqa E501
            self.make_moviment(**kwargs, is_published=True)
            print(f'Moviment {i + 1} created')  # Adiciona uma impressão para cada movimentação criada


        response = self.client.get(reverse("moves:difficulty", kwargs={'difficulty_id': 1},))  # noqa E501
        movement = response.context['moves']
        paginator = movement.paginator

        print(len(paginator.get_page(1)))
        self.assertEqual(paginator.num_pages, 3)
      #  self.assertEqual(len(paginator.get_page(1)), 3)
      #  self.assertEqual(len(paginator.get_page(2)), 3)
      #  self.assertEqual(len(paginator.get_page(3)), 2)
