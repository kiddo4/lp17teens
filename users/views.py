from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from Baseapp.models import Category



def register(request):
	cats_menu = Category.objects.all()
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'Your Account has been created, please kindly login !')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render (request,'users/register.html',{'form':form,'cats_menu':cats_menu})

@login_required
def profile(request):
    cats_menu = Category.objects.all()
    if request.method == 'POST':
    	u_form=UserUpdateForm(request.POST,instance=request.user)
    	p_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    	if u_form.is_valid and p_form.is_valid():
    	     	u_form.save()
    	     	p_form.save()
    	     	messages.success(request,f'Your Account has been updated !')
    	     	return redirect('profile')
    else:
         		    u_form =UserUpdateForm(instance=request.user)
         		    p_form = ProfileUpdateForm(instance=request.user.profile)
         		    context = {
	             'u_form':u_form,
	             'p_form':p_form,
	             'cats_menu':cats_menu
	                               }
         		    
         		    return render(request, 'users/profile.html', context)
	        		    
	        		
                             
# Create your views here.
