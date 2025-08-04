from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


from django.contrib.auth.decorators import login_required

@login_required
def account_home(request):
    return render(request, 'accounts/account_home.html')


def logged_out(request):
    return render(request, 'registration/logged_out.html')
