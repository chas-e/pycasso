from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('art/', views.ArtList.as_view(), name='art_index'),
    path('art/create/', views.ArtCreate.as_view(), name='art_create')
]