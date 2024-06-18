from django.shortcuts import render, get_list_or_404, get_object_or_404
from handbook.models import Moves
# Create your views here.


def home(request):
    movement= Moves.objects.filter(is_published=True).order_by('-movement_id')
    return render(request, 'handbook/pages/index.html', context={
        'moves': movement,
    })

def move(request,movement_id):
    movement = get_object_or_404(Moves, movement_id=movement_id, is_published = True )
    return render(request, 'handbook/pages/move_detail.html', context={
        'move': movement,
        'is_detail_page':True,
    })

def difficulty_def(request, difficulty_id):
    difficultys = get_list_or_404(Moves.objects.filter(difficulty__id=difficulty_id, is_published=True)) 
    return render(request,"handbook/pages/difficulty.html" ,
                   context= {
                       'moves': difficultys,
                       'title': f'{difficultys[0].difficulty.difficulty} | Dificuldades '
                       })

def category_def(request, category_id):
    categorys = get_list_or_404(Moves.objects.filter(category__id=category_id, is_published=True).order_by('-movement_id'))
    return render(request, "handbook/pages/category.html",
                   context={
                       'moves':categorys,
                       'title': f'{categorys[0].category.category} | Categorias '
                       } )


