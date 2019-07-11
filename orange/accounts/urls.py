from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path('register/', views.register, name='register'),
    path('manage/', views.manage, name='manage'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('view/', views.view, name='view'),
    path('edit/', views.edit, name='edit'),
]
