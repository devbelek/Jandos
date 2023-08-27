from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book_Table
from django.contrib.auth.models import User


@login_required
def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


@login_required
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        date = request.POST.get('date')
        person = request.POST.get('person')

        if name != '' and email != '' and number != '' and date != '' and person != '':
            data = Book_Table(name=name, email=email, number=number, date=date, person=person)
            data.save()

    return render(request, 'main/contact.html')


def menu(request):
    return render(request, 'main/menu.html')


def signup_page(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'main/signup.html')


def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'main/login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')
