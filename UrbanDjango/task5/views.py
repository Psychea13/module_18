from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.
users = ['Anne', 'Harry', 'Sophie']
info = {}
context = {'info': info}


def registration(username, password, repeat_password, age, users):
    if username in users:
        return 'Пользователь уже существует.'
    if password != repeat_password:
        return 'Пароли не совпадают. Попробуйте еще раз.'
    if int(age) < 18:
        return 'Вы должны быть старше 18 лет.'
    return


def sign_up_by_django(request):

    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            error = registration(username, password, repeat_password, age, users)

            if error:
                info['error'] = error
                return render(request, 'fifth_task/registration_page.html', context)
            return HttpResponse(f'Приветствуем, {username}!')

    else:
        info['form'] = UserRegister()

    return render(request, 'fifth_task/registration_page.html', context)


def sign_up_by_html(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        error = registration(username, password, repeat_password, age, users)

        if error:
            info['error'] = error
            return render(request, 'fifth_task/registration_page.html', context)
        return HttpResponse(f'Приветствуем, {username}!')

    return render(request, 'fifth_task/registration_page.html', context)
