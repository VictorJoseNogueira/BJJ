from random import randint, choice, choices
from faker import Faker
import string

def generate_random_youtube_link():
    videos_links = [
    'https://www.youtube.com/embed/YPpAjIF7GpU?si=VwxaYXxhG7sOSJWJ',
    'https://www.youtube.com/embed/Br_rPX6amrA?list=PLgtHVv30qeezpWs0D0ucbF4qeKZaQ1R3X' ,
    'https://www.youtube.com/embed/bUfyMz4yTKg?list=PLgtHVv30qeezpWs0D0ucbF4qeKZaQ1R3X',
    'https://www.youtube.com/embed/SFmTFu8fHw0?list=PLgtHVv30qeezpWs0D0ucbF4qeKZaQ1R3X"3X',
    'https://www.youtube.com/embed/Qcc-OqcI29c?list=PLgtHVv30qeezpWs0D0ucbF4qeKZaQ1R3X',
    'https://www.youtube.com/embed/kx9j47OBTgw?list=PLgtHVv30qeezpWs0D0ucbF4qeKZaQ1R3X',
    'https://www.youtube.com/embed/3oUNhemPsuA?list=PLgtHVv30qeezpWs0D0ucbF4qeKZaQ1R3X',
    'https://www.youtube.com/embed/uQQcBTXj-88?list=PLgtHVv30qeezpWs0D0ucbF4qeKZaQ1R3X' 
    ]
    return choice(videos_links)

fake = Faker("pt_BR")

def rand_difficulty():
    difficultys = ['Intermediario', 'Iniciante', 'Avançado']
    return choice(difficultys)

def rand_category():
    categorys = ['Fundamentos', 'Defesa Pessoal', 'Raspagens', 'Ataques Laterais', 'Ataques nas Costas']
    return choice(categorys)


def move_card_detail():
    return {
        'move_id':fake.random_number(digits=2, fix_len=True) ,   
        'title': fake.sentence(nb_words=6),
        'difficulty': rand_difficulty(),
        'category': rand_category(),
        'movement_id': generate_random_youtube_link()
    }

if __name__ == '__main__':
    from pprint import pprint
    pprint(move_card_detail())

