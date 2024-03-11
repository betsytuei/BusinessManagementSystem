
from django.contrib import admin
from django.urls import path
from businessapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register,name = 'register'),
    path('login/', views.login,name = 'login'),
    path('index/', views.index,name = 'index'),
]
