from django.urls import path
from main import views as vs


urlpatterns = [
    path('', vs.home, name='home'),
    path('about/', vs.about, name='about'),
    path('contact/', vs.contact, name='contact'),
    path('menu/', vs.menu, name='menu'),
    path('login/', vs.login_page, name='login'),
    path('signup/', vs.signup_page, name='signup'),
]