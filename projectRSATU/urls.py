"""projectRSATU URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
# from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from RSATU1 import views

urlpatterns = [
    # path('', views.index, name='home'),
    path('admin/', admin.site.urls),

    path('about', views.about),
    path('contact', views.contact),
    path('blog', views.PostListView.as_view(), name='blog'),
    re_path(r'blog/post/(?P<pid>\d+)', views.post),
    re_path(r'tag/(?P<curTag>\w+)', views.tags),

    # re_path(r'^login/$', auth_views.login, name='login'),
    # re_path(r'^logout/$', auth_views.logout, name='logout'),
    # re_path(r'^admin/', admin.site.urls)

    re_path(r'^accounts/login/$', views.user_login, name='login'),
    re_path(r'^accounts/register/$', views.register, name='register'),

    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('accounts/', include('django.contrib.auth.urls')),

    re_path(r'^chats/$', views.get_chat_list, name='chat_list'),
    re_path(r'^chats/create/(?P<user_id>\d+)/$', views.create_dialog, name='create_dialog'),
    re_path(r'^chats/(?P<chat_id>\d+)/$', views.MessagesView.as_view(), name='messages'),
]
