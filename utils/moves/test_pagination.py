from handbook.tests.test_move_base import MovesTestBase
from utils.moves.pagination import make_pagination_range


class Pagination_Test(MovesTestBase):

    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,

        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_first_range_is_static_if_current_page_is_less_than_middle_range(self):  # noqa E501
        # current_ page == 1 - qty_pages == 2 - middle_page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,

        )['pagination']
        # current_ page == 2 - qty_pages == 2 - middle_page = 2
        self.assertEqual([1, 2, 3, 4], pagination)
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=2,

        )['pagination']
        # current_ page == 3 - qty_pages == 2 - middle_page = 2
        # range shoud change
        self.assertEqual([1, 2, 3, 4], pagination)
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=3,

        )['pagination']
        self.assertEqual([2, 3, 4, 5], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=4,

        )['pagination']
        self.assertEqual([3, 4, 5, 6], pagination)

    def test_make_sure_middle_range_is_correct(self):  # noqa E501
        # current_ page == 3 - qty_pages == 2 - middle_page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=3,

        )['pagination']
        self.assertEqual([2, 3, 4, 5], pagination)
        # current page 10
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=10,

        )['pagination']
        self.assertEqual([9, 10, 11, 12], pagination)
        # current page 15
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=15,

        )['pagination']
        self.assertEqual([14, 15, 16, 17], pagination)

    def test_make_pagination_ranges_is_static_when_last_page_is_next(self):
        # current page 19
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=19,

        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)
        # current page 20
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=20,

        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)
        # current page 21
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=21,

        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)
