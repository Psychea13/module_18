from django.shortcuts import render


# Create your views here.
def menu(request):
    return render(request, 'fourth_task/menu.html', context)


def platform(request):
    text1 = 'Главная страница'
    text2 = 'Тут будет контент'
    context = {
        'text1': text1,
        'text2': text2,
    }
    return render(request, 'fourth_task/platform.html', context)


def games(request):
    text1 = 'Игры'
    text2 = 'Купить'
    context = {
        'text1': text1,
        'text2': text2,
        'games': ['Atomic Heart', 'Cyberpunk 2077', 'S.T.A.L.K.E.R. 2'],
    }
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    text1 = 'Корзина'
    text2 = 'Извините, ваша корзина пуста'

    context = {
        'text1': text1,
        'text2': text2,
    }
    return render(request, 'fourth_task/cart.html', context)
