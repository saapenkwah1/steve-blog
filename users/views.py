from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    """Register a new User"""
    #if post data is not submitted; display blank registration form
    if request.method != "POST":
        form = UserCreationForm()
    else:
        #Post data is submitted; process data
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            #log the user in an and redirect user to home page
            return redirect('blogs:index')
    #Display invalid or blank registration form
    context = {'form':form}
    return render(request, 'registration/register.html', context)
        

