from django.shortcuts import render, redirect
from accounts.forms import SignUpForm

# Create your views here.

def register(request):

    # check if we have a filled in form
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            # If forms are valid add data to the database
            form.save()
            return redirect('/')
    else:
        form = SignUpForm()

    args = {'form': form}
    return render(request, 'accounts/register.html', args)

def manage(request):
    return render(request, 'accounts/manage.html')

def about(request):
    return render(request, 'accounts/about.html')

def contact(request):
    return render(request, 'accounts/contact.html')

def view(request):
    current_user = request.user

    if current_user.is_authenticated:
        return render(request, 'accounts/view.html')    
    
    else:
        return redirect('/')
        