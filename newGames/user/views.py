from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from user.forms import CreateUserForm, ChangeUserForm, ChangeUserAvatarForm
# Create your views here.
from django.urls import reverse
# from main.views import Post, PostLike
from user.models import User, FriendUser, UserPhoto


def user_login(request):
    if request.POST:
        if 'email' in request.POST and request.POST['email']:
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('new:index'))
            else:
                error = 'Не правельно введены данные.'
                context = {
                    'error': error,
                }
                return render(request, 'user/login.html', context)
        elif 'username' in request.POST and request.POST['username']:
            name = request.POST['username']
            user = User.objects.filter(name=name)
            user1 = User.objects.filter(email=name)
            if user or user1:
                error1 = 'Данное имя занято.'
                context = {
                    'error1': error1,
                }
                return render(request, 'user/login.html', context)
            else:
                request.session['name'] = name
                return HttpResponseRedirect(reverse('user:register'))

    return render(request, 'user/login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('new:index'))


def user_register(request):
    name = request.session.get('name', 'Нет имя')
    label_name = 'Hi! ' + name
    error = None
    if request.method == 'POST':
        register_form = CreateUserForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            email = request.POST['email']
            password = request.POST['password1']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('new:index'))
        else:
            error = 'Ошибка'
            register_form = CreateUserForm(request.POST if request.POST else None)
            for reg in register_form:
                if reg.name == 'name':
                    reg.initial = name
                    label_name = 'Hi! ' + name

    else:
        register_form = CreateUserForm()
        for reg in register_form:
            if reg.name == 'name':
                reg.initial = name
                label_name = 'Hi! ' + name

    context = {
        'register_form': register_form,
        'name': name,
        'label_name': label_name,
        'error': error,
    }
    return render(request, 'user/register.html', context)


def user_edit(request):
    if request.method == 'Post':
        edit_form = ChangeUserForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('user:edit'))
    else:
        edit_form = ChangeUserForm(instance=request.user)

    context = {
        'edit_form': edit_form,
    }
    return render(request, 'user/edit.html', context)


def user_profile(request, url_id=None):
    pass
    # if id:
    #     prof = User.objects.filter(id=id)
    #     try:
    #         if prof[0].is_active:
    #             user_friend = FriendUser.objects.filter(user_friend_id=id)
    #             user_post = Post.objects.filter(author__id=id)
    #             user_photo = UserPhoto.objects.filter(user_id=id)
    #             user_like = PostLike.objects.filter(post__author=id)
    #             context = {
    #                 'prof': prof,
    #                 'user_friend': user_friend,
    #                 'user_photo': user_photo,
    #                 'user_post': user_post,
    #                 'user_like': user_like,
    #             }
    #         else:
    #             text_none = 'Пользователь удалил свой аккаунт ☹'
    #             context = {
    #                 'text_none': text_none,
    #             }
    #     except:
    #         text_none = 'Упс...😳 Пользователь не найден!'
    #         context = {
    #             'text_none': text_none,
    #         }
    # else:
    #     text_none = 'Упс...😳 Пользователь не найден!'
    #     context = {
    #         'text_none': text_none,
    #     }
    # return render(request, 'user/profile.html', context)
