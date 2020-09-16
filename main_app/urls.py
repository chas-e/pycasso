from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('art/', views.ArtList.as_view(), name='art_index'),
    path('art/create/', views.ArtCreate.as_view(), name='art_create'),
    path('art/<int:pk>/', views.ArtDetail.as_view(), name='art_detail'),
    path('art/<int:pk>/update/', views.ArtUpdate.as_view(), name='art_update'),
    path('art/<int:pk>/delete/', views.ArtDelete.as_view(), name='art_delete'),
]