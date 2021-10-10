from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='cookie.create'),
    path('read/', views.read, name='cookie.read'),
    path('update/<int:cookieId>', views.update, name='cookie.update'),
    path('delete/<int:cookieId>', views.delete, name='cookie.delete')
]