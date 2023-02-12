from django.shortcuts import render
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect, HttpResponse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from accounts.models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            #user bor bo'lsa
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Successfuly login')
                else:
                    return HttpResponse('Error login siz blockdasiz!')
            else:
                form = LoginForm()
                context = {'form': form}
                return HttpResponse('Login yoki password xato')
        else:
            return render(request, 'account/login.html', context=context)
    else:
        form = LoginForm()
        context = {'form': form}
        return render(request, 'registration/login.html', context=context)

@login_required
def dashboard_view(request):
    user = request.user
    profile_info = Profile.objects.filter(user=request.user)[0]
    context = {
        'user': user,
        'profile_info':profile_info
    }
    return render(request, 'pages/dashboard.html', context=context)

def user_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'registration/register_done.html', context={'new_user': new_user})
        else:
            form = UserRegistrationForm()
            return render(request, 'registration/register.html', context={'form': form})
    else:
        form = UserRegistrationForm()
        return render(request, 'registration/register.html', context={'form': form})
    
@login_required
def edit_user(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse_lazy('edit_profle'))
        else:
            user_form = UserEditForm()
            profile_form = ProfileEditForm()
            
            context = {'user_form': user_form, 'profile_form': profile_form}
            
            return render(request, 'registration/edit_profile.html', context=context)
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        
        context = {'user_form': user_form, 'profile_form': profile_form}
        
        return render(request, 'registration/edit_profile.html', context=context)