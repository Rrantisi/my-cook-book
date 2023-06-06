from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login


def home(request):
  return render(request, 'home.html')

def signup(request):
    error_message = ''
    # POST request
    if request.method == 'POST':
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/') #UPDATE IT
        else:
            error_message = 'Invalid signup - try again'
    # GET request
    form = UserCreationForm() 
    return render(request, 'registration/signup.html', 
    {'form': form,
    'error': error_message}
    )
