from django.urls import resolve, reverse

from handbook import views
from unittest.mock import patch
from .test_move_base import MovesTestBase

# teste @skip("texto")
# self.fail('texto')


class Moves_home_views_test(MovesTestBase):
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

    def test_move_home_template_dont_load_movements_not_published(self):
        """ teste movement is_published False dont Show"""
        # need movement
        self.make_moviment(is_published=False)
        response = self.client.get(reverse("moves:home"))
        self.assertIn('Administrador esta preguiçoso mande ele aprovar as tecnicas logo', response.content.decode('utf-8'))  # noqa E501

    @patch('handbook.views.PER_PAGE', new=3)
    def test_move_home_is_paginated(self):

        for i in range(8):
            kwargs = {'title_slug': f'r{i}', 'author_data': {'username': f'ú{i}'}}  # noqa E501
            self.make_moviment(**kwargs)

        response = self.client.get(reverse('moves:home'))
        movement = response.context['moves']
        paginator = movement.paginator

        self.assertEqual(paginator.num_pages, 3)
        self.assertEqual(len(paginator.get_page(1)), 3)
        self.assertEqual(len(paginator.get_page(2)), 3)
        self.assertEqual(len(paginator.get_page(3)), 2)
