from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/admin/')

        return render(request, 'myauth/login.html')

    user_name = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=user_name, password=password)
    if user is not None:
        login(request, user)
        return redirect('/admin/')

    return render(request, 'myauth/login.html', {'error': 'Invalid login credentials'})


def logout_view(request: HttpRequest):
    logout(request)
    return redirect(reverse('myauth:login'))


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('myauth:login')
    http_method_names = ['get', 'post']
    # Инфа, что это работает неккоретко имеется, чекай учебник

def set_cookie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse('Cookie set')
    response.set_cookie('fizz', 'buzz', max_age=3600)
    return response


def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get('fizz', 'default value')
    return HttpResponse(f'Cookie value: {value!r}')


def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session['foobar'] = 'spameggs'


def get_session_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get('foobar', 'default')
    return HttpResponse(f'Session value: {value!r}')
