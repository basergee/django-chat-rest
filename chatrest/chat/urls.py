from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from rest_framework import routers

from .views import UserSignupView
from .serializers import UserViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    # path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(template_name='login.html'),
         name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'),
         name='logout'),
    path('signup/', UserSignupView.as_view(), name='signup'),
    # path('profile/', UserProfileView.as_view(), name='profile'),
    path('', include(router.urls)),
]
