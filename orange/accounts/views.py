from django.shortcuts import render, redirect
from accounts.forms import SignUpForm, UserInfoForm

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

def view(request):
    current_user = request.user

    if current_user.is_authenticated:
        return render(request, 'accounts/view.html')    
    
    else:
        return redirect('/')

def edit(request):
    current_user = request.user

    if current_user.is_authenticated:

        # if post, save user details
        if request.method == 'POST':
            user_info_form = UserInfoForm(request.POST, request.FILES, instance=current_user)
            if user_info_form.is_valid():
                user_info_form.save()
            return redirect('/accounts/view')
        else:
            user_info_form = UserInfoForm(instance=current_user)

        args = {
            'form': user_info_form
        }

        return render(request, 'accounts/edit.html', args)
    
    else:
        return redirect('/')
