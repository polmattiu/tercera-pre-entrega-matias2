from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.mi_vista, name='inicio'),
    path('lista-de-gastos/', views.lista_de_gastos, name='lista_de_gastos'),
    path('gastos-realizados/', views.gastos_realizados, name='gastos_realizados'),
]
