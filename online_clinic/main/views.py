from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
def index_page(request):
    print('request is accepted')

    context = {
        'username': 'Test',

        }
    return render(request, 'main/index.html', context)

def doctors_page(request):
    return render(request, 'main/doctors.html', {} )

def price_page(request):
    return render(request, 'main/price.html', {} )

def contacts_page(request):
    return render(request, 'main/contacts.html', {} )

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse("main:profile"))

        return render(request, 'main/login.html', {"error": "Неверный Логин/Пароль"})
    return render(request, 'main/login.html', {})

def register_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            email = request.POST.get('email', None)
            first_name = request.POST.get('first_name', None)
            last_name = request.POST.get('last_name', None)
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
            )
            return redirect(reverse("main:login"))
        except Exception as exc:
            print('При создании профиля произошла ошибка', request.POST, exc)
            error = {
                "error_code": exc,
                "message": "Проверьте корректность введенных данных"
            }
            return render(request, "main/register.html", {"error": error})

    return render(request, "main/register.html", {})

def profile_page(request):
    if request.user.is_authenticated:
        return render(request, "main/profile.html", {})
    return redirect(reverse('main:login'))

def logout_view(request):
    logout(request)
    return redirect(reverse("main:index_page"))

def zapic_page(request):
    if request.method == "POST":
        try:
            name = request.POST.get('name', None)
            otdel = request.POST.get('otdel', None)
            phone = request.POST.get('phone', None)
            user = User.objects.create_user(
                name=name,
                otdel=otdel,
                phone=phone,
            )
            return redirect(reverse("main:zapic"))
        except Exception as exc:
            print('При записи на прием произошла ошибка', request.POST, exc)
            error = {
                "error_code": exc,
                "message": "Проверьте корректность введенных данных"
            }
            return render(request, "main/zapic.html", {"error": error})

    return render(request, "main/zapic.html", {})