from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import *



@login_required
def profile(request):
	user = request.user
	context = {
		
	}
	return render(request, "users/profile.html", context)

def login_user(request):
	if request.user.is_authenticated:
		return redirect('index')

	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		remember_me = request.POST.get('remember_me')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			if not remember_me:
				request.session.set_expiry(0)
			return redirect('index')
		
		else:
			messages.warning(request, "Username or password is incorrect!")

	context = {}
	return render(request, "users/login.html")

def register_user(request):
	if request.user.is_authenticated:
		return redirect('index')
	form = RegisterForm()

	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Your account has been registered, You can now login!")
			return redirect('login')

	context = {
		"form": form
	}
	return render(request, "users/register.html", context)

@login_required
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)  # Important!
			messages.success(request, 'Your password was successfully updated!')
			return redirect('change_password')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = PasswordChangeForm(request.user)

	context = {
		'form': form
	}
	return render(request, 'users/change_password.html', context)

def logout_user(request):
	logout(request)
	messages.info(request, "You have been logged out successfully!")
	return redirect('login')

def reset_password(request):
	if request.user.is_authenticated:
		return redirect('index')
	return render(request, "users/reset_password.html")

@login_required
def settings_page(request):
	
	context = {
		'gsc_connected': True
	}
	return render(request, 'users/settings.html', context)
