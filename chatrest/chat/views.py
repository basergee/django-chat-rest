from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView

from .forms import UserSignupForm


class UserSignupView(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


class IndexView(TemplateView):
    template_name = "chat/index.html"


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
