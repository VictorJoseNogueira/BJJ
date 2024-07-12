from django.urls import resolve, reverse

from handbook import views

from .test_move_base import MovesTestBase

# teste @skip("texto")
# self.fail('texto')


class Moves_search_views_test(MovesTestBase):
    # Search
    def test_move_search_uses_correct_view_function(self):
        resolved = resolve(reverse("moves:search"))
        self.assertIs(resolved.func, views.search_def)

    def test_move_search_loads_correct_template(self):
        response = self.client.get(reverse("moves:search")+"?q=TESTE")
        self.assertTemplateUsed(response, 'handbook/pages/search.html')

    def test_move_search_raises_404_if_no_search_term(self):
        response = self.client.get(reverse("moves:search"))
        self.assertEqual(response.status_code, 404)

    def test_move_search_term_is_on_page_title_and_escaped(self):
        response = self.client.get(reverse("moves:search")+"?q=<teste>")
        self.assertIn(
            'Pesquisa por &quot;&lt;teste&gt;&quot;',
            response.content.decode('utf-8')
        )

    def test_move_search_can_find_movement_by_title(self):
        title = 'this is a movement test one'
        title_2 = 'this is a movement test two'

        movement1 = self.make_moviment(
            title_slug='one',
            title=title,
            author_data={"username": "one"},
        )
        movement2 = self.make_moviment(
            title_slug='two',
            title=title_2,
            author_data={"username": "two"},
        )
        search_url = reverse("moves:search")
        response_1 = self.client.get(f'{search_url}?q={title}')
        response_2 = self.client.get(f'{search_url}?q={title_2}')
        response_both = self.client.get(f'{search_url}?q=this')

        self.assertIn(movement1, response_1.context['moves'])
        self.assertNotIn(movement2, response_1.context['moves'])

        self.assertIn(movement2, response_2.context['moves'])
        self.assertNotIn(movement1, response_2.context['moves'])

        self.assertIn(movement1, response_both.context['moves'])
        self.assertIn(movement2, response_both.context['moves'])
