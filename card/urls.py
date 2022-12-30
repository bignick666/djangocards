from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'card'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('cards/', views.profile_cards, name='cards'),
    path('cards/new_card', views.new_card, name='new_card'),
    path('cards/delete_card/<int:id>', views.delete_card, name='delete_card'),
    path('cards/deactivate_card/<int:id>', views.deactivate_card, name='deactivate_card'),
    path('cards/activate_card/<int:id>', views.activate_card, name='activate_card'),
    # path('login/', views.user_login, name='login')
]