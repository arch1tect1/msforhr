from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
from .forms import SignUpForm, EditProfileForm
from django.conf import settings
from .models import File
from .forms import FileAddForm



def index(request):
    return render(request, 'authenticate/index.html')


def home(request):
    files = File.objects.all()
    return render(request, 'authenticate/home.html', {'files': files})


def add_file(request):
    if request.method == 'POST':
        form = FileAddForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, "File added successfully")
            return redirect('home')
    else:
        form = FileAddForm()
    return render(request, 'authenticate/add_file.html', {'form': form})


def delete_file(request, pk):
    if request.method == 'POST':
        file = get_object_or_404(File, pk=pk)
        file.delete()
        messages.success(request, "File deleted successfully")
        return redirect('home')
    else:
        return redirect('home')


def login_user (request):
	if request.method == 'POST': #if someone fills out form , Post it 
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:# if user exist
			login(request, user)
			messages.success(request,('Youre logged in'))
			return redirect('home') #routes to 'home' on successful login  
		else:
			messages.success(request,('Error logging in'))
			return redirect('login') #re routes to login page upon unsucessful login
	else:
		return render(request, 'authenticate/login.html', {})


def logout_user(request):
	logout(request)
	messages.success(request,('Youre now logged out'))
	print('Youre now logged out')
	return redirect('home')


def register_user(request):
	if request.method =='POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request,user)
			messages.success(request, ('Youre now registered'))
			return redirect('home')
	else: 
		form = SignUpForm() 

	context = {'form': form}
	return render(request, 'authenticate/register.html', context)


def edit_profile(request):
	if request.method =='POST':
		form = EditProfileForm(request.POST, instance= request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('You have edited your profile'))
			return redirect('home')
	else: 		#passes in user information 
		form = EditProfileForm(instance= request.user) 

	context = {'form': form}
	return render(request, 'authenticate/edit_profile.html', context)
	#return render(request, 'authenticate/edit_profile.html',{})


def change_password(request):
	if request.method =='POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, ('You have edited your password'))
			return redirect('authenticate/home.html')
	else: 		#passes in user information 
		form = PasswordChangeForm(user= request.user) 

	context = {'form': form}
	return render(request, 'authenticate/change_password.html', context)


def privacy(request):
	return render(request, 'authenticate/privacy.html')


def terms(request):
	return render(request, 'authenticate/terms.html')
