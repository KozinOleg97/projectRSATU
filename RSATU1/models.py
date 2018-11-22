from django.db import models

# Create your models here.
from django.db import models
from django.utils.datetime_safe import datetime

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm



class Tag(models.Model):
    title = models.CharField(max_length=100)


class Post(models.Model):
    header = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    date = models.DateField(default='')
    text = models.TextField(default='')
    tag = models.ManyToManyField(Tag)



class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)