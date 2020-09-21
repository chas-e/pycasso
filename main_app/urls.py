from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('art/', views.ArtList.as_view(), name='art_index'),
    path('art/create/', views.ArtCreate.as_view(), name='art_create'),
    path('profile/create/', views.ProfileCreate.as_view(), name='profile_create'),
    path('profile/<int:user_id>/', views.profile_detail, name='profile_detail'),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update'),
    path('art/<int:pk>/', views.ArtDetail.as_view(), name='art_detail'),
    path('art/<int:pk>/update/', views.ArtUpdate.as_view(), name='art_update'),
    path('art/<int:pk>/delete/', views.ArtDelete.as_view(), name='art_delete'),
    path('gallery/', views.gallery_index, name='gallery_index'),
    path('gallery/<int:art_id>/', views.gallery_detail, name='gallery_detail'),
    path('art/<int:art_id>/add_comment/', views.add_comment, name='add_comment'),
    path('gallery/<int:art_id>/comment/<int:pk>/update/', views.CommentUpdate.as_view(), name="comment_update"),
    path('gallery/<int:art_id>/comment/<int:pk>/delete/', views.CommentDelete.as_view(), name="comment_delete"),
    path('paint/', views.paint, name='paint'),
    path('files/', views.files, name='files'),
    path('paint_chat/', views.paint_index, name='paint_index')
]