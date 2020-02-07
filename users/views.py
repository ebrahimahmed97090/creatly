from django.shortcuts import render
from users.models import User
# from . import forms
from users.forms import NewUserForm, NewUserInfoForm

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


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
    return render(request, 'home.html')


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

    return render(request, 'registration.html', {'userform': userform, 'userinfo': userinfo, 'registered': registered})


def example(request):
    my_dict = {'insert_me': "Hello I am from views.py"}
    return render(request, 'examples.html', context=my_dict)


@login_required
def UWl(request):
    my_dict = {'Add_opt': '<span class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="far fa-ellipsis-v"></i></span><div class="dropdown-menu" aria-labelledby="dropdownMenuButton"><a class="dropdown-item" href="#">Edit</a><a class="dropdown-item" href="#">Up</a><a class="dropdown-item" href="#">Down</a><a class="dropdown-item" href="#">Remove</a></div>'}
    return render(request, 'User_Wlist.html', context=my_dict)


def usershome(request):
    my_dict = {'insert_me': "Hello I am from views.py"}
    return render(request, 'usershome.html', context=my_dict)


def user_login(request):
    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            # Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request, user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('home'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        # Nothing has been provided for username or password.
        return render(request, 'userlogin.html', {})


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('home'))
def tmps(request):
    my_dict = {'insert_me': "Hello I am from views.py"}
    return render(request, 'Template_store.html', context=my_dict)
