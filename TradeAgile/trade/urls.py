from django.urls import path
from . import views

# URL para a determinada página, mapeada para a função que está em views.py
urlpatterns = [
    path('', views.login_view, name='login'),  # Página de login
    path('home/', views.home, name='home'),  # Página inicial
    path('cadastro_clientes/', views.cadastro_clientes, name='cadastro_clientes'),  # Cadastro de clientes
    path('demonstrativo_tabelas/', views.demonstrativo_tabelas, name='demonstrativo_tabelas'),  # Demonstrativo de tabelas
    path('galeria_produtos/', views.galeria_produtos, name='galeria_produtos'),  # Galeria de produtos
    path('realizar_venda/', views.realizar_venda, name='realizar_venda'),  # Realização de venda
    path('venda_realizada/', views.venda_realizada, name='venda_realizada'),  # Confirmação de venda
    path('register/', views.register_view, name='register'),  # Registro de usuário
]