"""
URL configuration for devoted project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from display.views import index, dashboard, budget, journal, assets, notifications, login, user_login, user_signup, add_journal

urlpatterns = [
    path('', index, name="index"),
    path('dashboard/', dashboard, name="dashboard"),
    path('budget/', budget, name="budget"),
    path('journal/', journal, name="journal"),
    path('assets/', assets, name="assets"),
    path('notifications/', notifications, name="notifications"),
    path('login/', login, name="login"),
    path('user_login/', user_login, name="user_login"),
    path('user_signup/', user_signup, name="user_signup"),
    path('add_journal/', add_journal, name="add_journal"),
    path('admin/', admin.site.urls),
]
