from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import ProfileForm, CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, "Successfully added!")
            return redirect('accounts:login')
        else:
            messages.error(request, "Please fill in all the fields.")
    else:
        user_form = CustomUserCreationForm()
        profile_form = ProfileForm()
    context = {"user_form": user_form, "profile_form": profile_form}
    return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged In successful")
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, 'accounts/login.html', context)


