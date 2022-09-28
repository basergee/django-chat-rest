from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView
from django.http import HttpResponseNotFound

from .forms import UserSignupForm
from .models import Room


class UserSignupView(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


class IndexView(TemplateView):
    template_name = "chat/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = Room.objects.all()
        return context


def room(request, room_name):
    if Room.objects.filter(name=room_name).exists():
        return render(request, 'chat/room.html', {
            'room_name': room_name
        })
    else:
        return HttpResponseNotFound(f'<h1>Комнаты c именем \"{room_name}\" '
                                    f'не существует</h1>')
