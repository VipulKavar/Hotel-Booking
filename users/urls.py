from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users import views

from users.forms import UserLoginForm

app_name = 'users'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('list', views.UserListView.as_view(), name='user_list'),
    path('update/<int:pk>/', views.UserUpdateView.as_view(), name='user_update'),
    path('create/', views.UserCreateView.as_view(), name='user_create'),
    path('delete/<int:pk>/', views.UserDeleteView.as_view(), name='user_delete'),
    path('profile/<int:pk>/', views.UserProfileView.as_view(), name='user_profile'),
    path('login/', LoginView.as_view(template_name="users/user_login.html"), name='user_login'),
    path('logout/', LogoutView.as_view(template_name='users/user_logout.html'), name='user_logout'),
    path('forbidden/', views.ForbiddenView.as_view(), name='user_forbidden'),
]
