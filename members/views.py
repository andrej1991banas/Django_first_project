
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




def view_name(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def members(request):

    mymembers= Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers
    }
    return HttpResponse(template.render(context, request))



def details(request, id):

    mymember = Member.objects.get(id=id)
    template = loader.get_template ('details.html')
    context = {
        'mymember' : mymember,
    }
    return HttpResponse(template.render(context, request))



def main(request):

    template= loader.get_template('main.html')
    return HttpResponse(template.render())



def testing(request):

    mymembers = Member.objects.all().values()
    return render(request, 'test2.html', {'mymembers': mymembers})

##################################################

# def homepage(request):
#     return render(request, 'homepage.html')

def register(request):
    form = CreateUserForm()
    if request.method =="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mylogin')

    return render(request, 'register.html', {'registerform': form})



def my_login(request):

    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return redirect('mylogin')
    context = {'loginform': form,}

    template = loader.get_template('my_login.html')
    return render(request, 'my_login.html', context)

@login_required(login_url="mylogin")
def dashboard(request):

    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render())


def user_logout(request):

    auth.logout(request)
    return redirect('mylogin')

