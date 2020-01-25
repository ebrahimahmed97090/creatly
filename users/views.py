from django.shortcuts import render
from django.http import HttpResponse
from users.models import User


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
    my_dict = {'insert_me': "Hello I am from views.py"}
    return render(request, 'registration.html', context=my_dict)


def example(request):
    my_dict = {'insert_me': "Hello I am from views.py"}
    return render(request, 'examples.html', context=my_dict)
