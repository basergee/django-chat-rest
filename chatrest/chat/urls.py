from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import UserSignupView


urlpatterns = [
    # path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(template_name='login.html'),
         name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'),
         name='logout'),
    path('signup/', UserSignupView.as_view(), name='signup'),
    # path('profile/', UserProfileView.as_view(), name='profile'),
]
