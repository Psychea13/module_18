from django.shortcuts import render


# Create your views here.
def platform(request):
    title = 'Игровая платформа'
    text1 = 'Главная страница'
    text2 = 'Главная'
    text3 = 'Магазин'
    text4 = 'Корзина'
    context = {
        'title': title,
        'text1': text1,
        'text2': text2,
        'text3': text3,
        'text4': text4,
    }
    return render(request, 'third_task/platform.html', context)


def games(request):
    title = 'Игровая платформа'
    text1 = 'Игры'
    text2 = 'Atomic Heart'
    text3 = 'Cyberpunk 2077'
    text4 = 'S.T.A.L.K.E.R. 2: Heart of Chornobyl'
    text5 = 'Купить'
    text6 = 'Вернуться на главную страницу'
    context = {
        'title': title,
        'text1': text1,
        'text2': text2,
        'text3': text3,
        'text4': text4,
        'text5': text5,
        'text6': text6,
    }
    return render(request, 'third_task/games.html', context)


def cart(request):
    title = 'Игровая платформа'
    text1 = 'Извините, ваша корзина пуста'
    text2 = 'Вернуться на главную страницу'

    context = {
        'title': title,
        'text1': text1,
        'text2': text2,
    }
    return render(request, 'third_task/cart.html', context)
