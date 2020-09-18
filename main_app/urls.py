from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('art/', views.ArtList.as_view(), name='art_index'),
    path('art/create/', views.ArtCreate.as_view(), name='art_create'),
    path('profile/create/', views.ProfileCreate.as_view(), name='profile_create'),
    path('profile/<int:user_id>/', views.profile_detail, name='profile_detail'),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update')
]