from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileForm

from django.contrib.auth import authenticate, login, logout
from  django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pics' in request.FILES:
                profile.picture = request.FILES['profile_pics']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'basic_app/registration.html',
                              {'user_form': user_form,
                              'profile_form': profile_form,
                              'registered': registered})
def mydef_user_login(request):
    if request.method == "POST":
        username = request.POST.get('username_createdbyme')
        password = request.POST.get('password_createdbyme')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
                # return HttpResponseRedirect(reverse('special'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("SOMEONE TRIED TO LOGIN AND FAILED")
            print('{} - {}'.format(username, password))
            return HttpResponse("INVALID LOGIN DETAILS")
    else:
        return render(request, 'basic_app/login.html')


@login_required
def correct_login_msg(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def mydef_user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
