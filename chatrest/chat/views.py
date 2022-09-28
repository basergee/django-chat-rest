from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView, UpdateView
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)

from .forms import UserSignupForm, UserEditForm
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


@login_required
def room(request, room_name):
    if Room.objects.filter(name=room_name).exists():
        room = Room.objects.get(name=room_name)
        return render(request, 'chat/room.html', {
            'room': room,
            # 'room_name': room_name,
            'members': room.current_users.all(),
        })
    else:
        return HttpResponseNotFound(f'<h1>Комнаты c именем \"{room_name}\" '
                                    f'не существует</h1>')


class UserEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'profile.html'
    success_url = reverse_lazy('index')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['is_not_author'] = not self.request.user.groups.filter(
    #         name='authors').exists()
    #     return context

    # Запрещаем авторизованному пользователю просматривать и править профили
    # других пользователей. Без этого пользователь мог указать ключ другого
    # пользователя в url и получить доступ к его профилю
    # Путь к странице имеет вид: /chat/profile/5/, где 5 -- это ключ в
    # базе пользователей. Авторизованный пользователь должен иметь доступ
    # только к своему профилю. Если он пробует получить доступ к чужому,
    # то будет ошибка '403 Forbidden'
    def test_func(self):
        return int(self.request.path.split('/')[-2]) == self.request.user.pk
