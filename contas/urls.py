from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('formaspagamento', views.formasPagamento, name='formaspagamento'),
    path('classreceber', views.classReceber, name='classreceber'),
    path('classpagar', views.classPagar, name='classpagar'),
    path('pagar', views.pagar, name='pagar'),
    path('receber', views.receber, name='receber'),
]
