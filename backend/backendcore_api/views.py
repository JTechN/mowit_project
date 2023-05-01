
# Rest_Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
#from rest_framework.decorators import api_view


# Django Contrib
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Django shortcuts
from django.shortcuts import HttpResponse, get_object_or_404, render, redirect

# Django views
from django.views import generic
from django.views.generic import DetailView

# Model
# from .models import RatingSystem

# Contractor
from Contractor.models import Service

# Customer
from Contractor.forms import RequestServiceForm, RequestServiceUpdateForm
from Contractor.models import RequestService

from .forms import NewUserForm, UserUpdateForm, ProfileUpdateForm, UserInfoUpdateForm

# Create your views here.

# Homepage
def homepage(request):
    user = request.user.id
    
    all_service = Service.objects.filter(account_id = user)
    Contractors = Service.objects.select_related('account').all()
    Customers = Group.objects.get(name='Customer').user_set.all()
    customer_request = RequestService.objects.filter(customer = user)
    contractor_request = RequestService.objects.filter(contractor = user)
     
    
		
    return render(request, 'homepage.html', {'services': all_service, 'Contractors': Contractors, 'Customers': Customers, 'customer_request': customer_request, 'contractor_request': contractor_request})

def update_request_status(request, contractor_id):
    request_service = get_object_or_404(RequestService, id=contractor_id)
    form = RequestServiceUpdateForm(instance=request_service)
    print(request.method)
    print(form.is_valid())
    print(form.errors)
    print(form.errors.as_data())
    
    if request.method == 'POST':
        form = RequestServiceUpdateForm(request.POST, instance=request_service)
        if form.is_valid():
            form.status = form.cleaned_data['status']
            form.save()
            return redirect('backendcore_api:homepage')
            
    return render(request, 'update_request_status.html', {'form': form, 'request_service': request_service})

# Registration Form
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			# group = Group.objects.get(name='groupname')
			group = form.cleaned_data['group']
			group.user_set.add(user)
			# user.groups.add(group)

			login(request, user)
			return redirect("backendcore_api:homepage")
	else:
		form = NewUserForm()
	return render (request=request, template_name='register.html', context={"register_form":form})

#Login Form
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				# messages.info(request, f"You are now logged in as {username}.")
				return redirect("backendcore_api:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	else:
		form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

#Logout Form
def logout_request(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('backendcore_api:login')

#Profile
@login_required
def profile_request(request):
  if request.method == 'POST':
    updateform = UserUpdateForm(request.POST, instance=request.user)
    profileform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    infoupdateform = UserInfoUpdateForm(request.POST, instance=request.user.userinfo)
    if updateform.is_valid() and profileform.is_valid() and infoupdateform.is_valid():
      updateform.save()
      profileform.save()
      infoupdateform.save()
      # messages.success(request, "Your Account Has Been Updated!")
      return redirect("backendcore_api:profile")

  else:
    updateform = UserUpdateForm(instance=request.user)
    profileform = ProfileUpdateForm(instance=request.user.profile)
    infoupdateform = UserInfoUpdateForm(instance=request.user.userinfo)

  context = {
		'updateform': updateform,
  	'profileform': profileform,
   	'infoupdateform': infoupdateform
	}

  return render(request, 'profile.html', context)
	# return render(request=request, template_name='profile.html')

#Add request in customer dashboard
def request_service(request):
    form = RequestServiceForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("backendcore_api:homepage")
    return render(request, 'customer_request_form.html', {'form':form})

def delete_service_request(request, customer_id):
    request_service = get_object_or_404(RequestService, id=customer_id)
    request_service.delete()
    return redirect('backendcore_api:homepage')




#Edit Profile
# def profile_edit(request, user_id):
# 	user = get_object_or_404(User, id=user_id)
# 	return render(request=request, template_name='profile_edit.html', context={"user": user})

# def rating(request: HttpResponse) -> HttpResponse:
#   ratings = RatingSystem.objects.filter(user = request.user).delete()
