from django.shortcuts import render, get_list_or_404, get_object_or_404
from handbook.models import Moves
from django.http import Http404
from django.db.models import Q
from utils.moves.pagination import make_pagination
import os
# Create your views here.

PER_PAGE = int(os.environ.get('PER_PAGE', 6))


def home(request):
    movement = Moves.objects.filter(is_published=True).order_by('-movement_id')  # noqa:E501
    page_object, pagination_range = make_pagination(request, movement, PER_PAGE)  # noqa:E501

    return render(request, 'handbook/pages/index.html', context={
        'moves': page_object,
        'pagination_range': pagination_range
        })  # noqa:E501


def move(request, movement_id):
    movement = get_object_or_404(Moves, movement_id=movement_id, is_published=True)  # noqa:E501

    return render(request, 'handbook/pages/move_detail.html', context={
        'move': movement,
        'is_detail_page': True,
    })


def difficulty_def(request, difficulty_id):
    difficultys = get_list_or_404(Moves.objects.filter(difficulty__id=difficulty_id, is_published=True))  # noqa:E501
    page_object, pagination_range = make_pagination(request, difficultys, PER_PAGE)  # noqa:E501

    return render(request, "handbook/pages/difficulty.html",
                  context={
                      'moves': page_object,
                      'pagination_range': pagination_range,
                      'title': f'{difficultys[0].difficulty.difficulty} | Dificuldades '})  # noqa:E501


def category_def(request, category_id):
    categorys = get_list_or_404(Moves.objects.filter(category__id=category_id, is_published=True).order_by('-movement_id'))  # noqa:E501
    page_object, pagination_range = make_pagination(request, categorys, PER_PAGE)  # noqa:E501

    return render(request, "handbook/pages/category.html",
                  context={
                      'moves': page_object,
                      'pagination_range': pagination_range,
                      'title': f'{categorys[0].category.category} | Categorias'})  # noqa:E501


def search_def(request):
    search_term = request.GET.get('q', '').strip()
    if not search_term:
        raise Http404()

    movement = Moves.objects.filter(
        Q(Q(title__icontains=search_term) | Q(category__category__icontains=search_term) | Q(difficulty__difficulty__icontains=search_term)), Q(is_published=True)  # noqa E501
    ).order_by('-movement_id')  # noqa E501
    page_object, pagination_range = make_pagination(request, movement, PER_PAGE)  # noqa:E501
    additional_url_query = f'&q={search_term}'
    context = {
        'page_title': f'Pesquisa por "{search_term}"',
        'search_term': search_term,
        'moves': page_object,
        'pagination_range': pagination_range,
        'additional_url_query': additional_url_query,
    }
    return render(request, 'handbook/pages/search.html', context=context,)
