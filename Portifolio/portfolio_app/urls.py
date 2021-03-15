from django.urls import path
from .views import *

app_name = 'portfolio_app'

urlpatterns = [
    path('', index, name='index'),
    path('portifolio/', portfolio, name='portfolio'),
    path('project_details/<int:pk>/', portfolio_item_detail, name='detail'),
    path('about/', about, name='about')

]
