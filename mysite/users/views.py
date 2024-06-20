from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, Your Account is created ')
            return redirect('login')
        else:
            print(form.errors)  # Print form errors to the console for debugging
            messages.error(request, 'Invalid Credentials. Please correct the errors below.')
    else:
        form = RegisterForm()
    return render(request,'users/register.html',{'form':form})
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request,f'Welcome {username}, Your Account is created ')
#             return redirect('food:index')
#     else:
#         form = UserCreationForm()
#     return render(request,'users/register.html',{'form':form})

@login_required
def profile_page(request):
    return render(request,'users/profile.html')