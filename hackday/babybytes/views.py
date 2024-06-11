from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Employee

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return render(request, 'signup.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken")
            return render(request, 'signup.html')
        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        return redirect('questions')
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def about_view(request):
    return render(request, 'about.html')

def message_view(request):
    return render(request, 'message.html')

@login_required
def account_view(request):
    return render(request, 'account.html')

@login_required
def home_view(request):
    return render(request, 'home.html')

def index_view(request):
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def question_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        state = request.POST.get('state')
        adoption = request.POST.get('adoption')
        adoption_money = request.POST.get('adoption_money', 'N/A')
        csection = request.POST.get('csection')

        name = str(name)  # Assuming name is a string
        state = str(state)  # Assuming state is a string
        adoption = str(adoption)  # Assuming adoption is a string
        adoption_money = str(adoption_money)  # Assuming adoption_money is a string
        csection = str(csection)

        if not all([name, state, adoption, csection]):
            messages.error(request, "All fields are required.")
            return render(request, "questions.html")
        
        user = Employee(
            username=request.user.username,
            name=name,
            state=state,
            adoption=adoption,
            reimbursement=adoption_money,
            csection=csection
        )
        user.save()

        return redirect('home')

    return render(request, "questions.html")