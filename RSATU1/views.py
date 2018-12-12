from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import generic, View

from RSATU1.models import Post, Tag, Chat, Message
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def index(request):
    # return HttpResponse("<h2>Главная</h2>")
    return render(request, "index.html")


def about(request):
    return HttpResponse("<h2>О сайте</h2>")


def contact(request):
    return HttpResponse("<h2>Контакты</h2>")


def post(reqest, pid):
    try:
        post = Post.objects.get(id=pid)
        tags = post.tag.all()
    except:
        return render(reqest, 'index.html')
    return render(reqest, 'post.html', {'post': post, 'tags': tags})


def tags(reqest, curTag):
    tag = Tag.objects.get(title=curTag)
    list = Post.objects.filter(tag=tag)

    return render(reqest, 'tags.html', {'post_list': list})


class PostListView(generic.ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'post_list.html'

    def get_queryset(self):
        return Post.objects.all()


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "home.html")
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def get_chat_list(request):
    if request.user.is_authenticated:
        list_of_chats = Chat.objects.filter(members__in=[request.user.id])
        return render(request, 'chat_list.html', {'list_of_chats': list_of_chats})
    else:
        list_of_chats = Chat.objects.filter(type='public')
        return render(request, 'chat_list.html', {'list_of_chats': list_of_chats})


def create_dialog(request):
    return None


def get_chat(request):
    # list_of_messages =
    return None


class MessagesView(View):
    def get(self, request, chat_id):
        try:
            chat = Chat.objects.get(id=chat_id)
            if request.user in chat.members.all():
                message_list = chat.message_set.filter(is_readed=False).exclude(author=request.user).update(
                    is_readed=True)

                message_list = chat.message_set
            else:
                chat = None
        except Chat.DoesNotExist:
            chat = None

        message_list = Message.objects.filter(chat=chat_id)
        return render(request, 'chat.html', {'user': request.user, 'chat': chat, "message_list": message_list})

    def post(self, request, chat_id):
        return None
    # form = MessageForm(data=request.POST)
    # if form.is_valid():
    #     message = form.save(commit=False)
    #     message.chat_id = chat_id
    #     message.author = request.user
    #     message.save()
    # return redirect(reverse('users:messages', kwargs={'chat_id': chat_id}))
