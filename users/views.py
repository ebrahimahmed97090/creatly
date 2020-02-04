from django.shortcuts import render
from django.http import HttpResponse
from users.models import User
from . import forms


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
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("form validation success.Prints in console")
            print("Name" + form.cleaned_data['name'])
            print("Email" + form.cleaned_data['email'])
            print("Text" + form.cleaned_data['text'])
        return render(request, 'registration.html', {'form': form})

    return render(request, 'registration.html', {'form': form})


def example(request):
    my_dict = {'insert_me': "Hello I am from views.py"}
    return render(request, 'examples.html', context=my_dict)
