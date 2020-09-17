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
    path('gallery/', views.gallery_index, name='gallery_index/'),
    path('gallery/<int:art_id>/', views.gallery_index, name='gallery_detail'),
    path('art/<int:art_id>/comment/create/', views.CommentCreate.as_view(), name='comment_create'),
]