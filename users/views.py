from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from .forms import UserRegistrationForm

# valid messages are:
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error

# Create your views here.
def register(request):
    if request.method == "POST":
      form = UserRegistrationForm(request.POST)
      if form.is_valid():
          form.save()
          username = form.cleaned_data.get('username')
          messages.success(request, f'Your Account has been created.  Your are able to login!')
          return redirect('login')
    else:        
      form = UserRegistrationForm()
    return render(request, 'users/registration.html',{'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')