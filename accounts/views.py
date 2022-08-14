from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import ContactForm, ProfileForm, CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib import messages


# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, "Account has been created please login")
            return redirect('accounts:login')
        else:
            messages.error(request, "Please fill in all the fields.")
    else:
        user_form = CustomUserCreationForm()
        profile_form = ProfileForm()
    context = {"user_form": user_form, "profile_form": profile_form}
    return render(request, 'accounts/register.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form)
    else:
        form = ContactForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/contact.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # messages.success(request, "Logged In successful")
            return redirect('/home/')
    else:
        form = AuthenticationForm(request)
        # form.fields['username'].widget.attrs['class'] = "bold"
        # form.fields['password'].widget.attrs['class'] = "bold"
    context = {
        "form": form
    }
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, "accounts/logout.html", {})


