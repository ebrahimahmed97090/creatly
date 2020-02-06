from django.shortcuts import render
from django.http import HttpResponse
from users.models import User
# from . import forms
from users.forms import NewUserForm, NewUserInfoForm


# Create your views here.


def prices(request):
    my_dict = {'insert_me': "Hello I am from views.py"}
    return render(request, 'priceplans.html', context=my_dict)


def contact(request):
    my_dict = {'insert_me': "Hello I am from views.py"}
    return render(request, 'contactus.html', context=my_dict)


def about(request):
    my_dict = {'insert_me': "Hello I am from views.py"}
    return render(request, 'aboutus.html', context=my_dict)


def home(request):
    users_list = User.objects.order_by('uid')
    users_dict = {'access_records': users_list}
    return render(request, 'home.html', context=users_dict)


def services(request):
    my_dict = {'insert_me': "Hello I am from views.py"}
    return render(request, 'services.html', context=my_dict)


def registration(request):
    registered = False
    if request.method == "POST":
        userform = NewUserForm(data=request.POST)
        userinfo = NewUserInfoForm(data=request.POST)

        if userform.is_valid() and userinfo.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()

            profile = userinfo.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(userform.errors, userinfo.errors)

    else:
        userform = NewUserForm()
        userinfo = NewUserInfoForm()

    return render(request, 'registration.html', {'userform': userform, 'userinfo': userinfo, 'registered':registered})


def example(request):
    my_dict = {'insert_me': "Hello I am from views.py"}
    return render(request, 'examples.html', context=my_dict)


def usershome(request):
    my_dict = {'insert_me': "Hello I am from views.py"}
    return render(request, 'usershome.html', context=my_dict)
