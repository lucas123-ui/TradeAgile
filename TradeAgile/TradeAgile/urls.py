from django.contrib import admin  # Traz a funcionalidade da página de administração do Django
from django.urls import path, include  # Traz funções para definir URLs e incluir URLs de outros arquivos

urlpatterns = [
    path('admin/', admin.site.urls),  # Quando alguém acessa '/admin/', mostre a página de administração
    path('', include('trade.urls')),  # Para qualquer outra URL, use as regras definidas em 'trade/urls.py'
]
