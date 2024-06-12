from django.shortcuts import render, redirect # type: ignore
from django.contrib import messages, auth # type: ignore
from django.contrib.auth.models import User # type: ignore

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'invalid login credentials!')
            return redirect('login')

    return render(request, 'accounts/login.html')

def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already used!')
                    return redirect('signup')
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                user.save()
                messages.success(request, 'You are registered successfully.')
                return redirect('dashboard')
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('signup')
    else:
        return render(request, 'accounts/signup.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You have been logged out.')

    return redirect('home')
