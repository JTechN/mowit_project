
# Rest_Framework
from django.shortcuts import render, get_object_or_404
from .models import Message
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
# from rest_framework.decorators import api_view


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
# from Contractor.forms import NewContractorForm
from Contractor.models import *

from .forms import NewUserForm, UserUpdateForm, ProfileUpdateForm, UserInfoUpdateForm

# Create your views here.

# Homepage


def homepage(request):
    return render(request=request, template_name='homepage.html')

def message(request):
    return render(request=request, template_name='messages.html')

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
    return render(request=request, template_name='register.html', context={"register_form": form})

# Login Form


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
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})

# Logout Form


def logout_request(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('backendcore_api:login')

# Profile


@login_required
def profile_request(request):
    if request.method == 'POST':
        updateform = UserUpdateForm(request.POST, instance=request.user)
        profileform = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        infoupdateform = UserInfoUpdateForm(
            request.POST, instance=request.user.userinfo)
        if updateform.is_valid() and profileform.is_valid() and infoupdateform.is_valid():
            updateform.save()
            profileform.save()
            infoupdateform.save()
            # messages.success(request, "Your Account Has Been Updated!")
            return redirect("backendcore_api:profile")

    else:
        updateform = UserUpdateForm(instance=request.user)
        profileform = ProfileUpdateForm(instance=request.user.profile)
        infoupdateform = UserInfoUpdateForm(instance=request.user)

    context = {
        'updateform': updateform,
        'profileform': profileform,
        'infoupdateform': infoupdateform
    }

    return render(request, 'profile.html', context)
    # return render(request=request, template_name='profile.html')

# Edit Profile
# def profile_edit(request, user_id):
# 	user = get_object_or_404(User, id=user_id)
# 	return render(request=request, template_name='profile_edit.html', context={"user": user})

# def rating(request: HttpResponse) -> HttpResponse:
#   ratings = RatingSystem.objects.filter(user = request.user).delete()


@login_required
def inbox(request):
    messages = request.user.received_messages.all()
    return render(request, 'messaging/inbox.html', {'messages': messages})


@login_required
def compose(request):
    if request.method == 'POST':
        recipient = User.objects.get(username=request.POST['recipient'])
        message = Message(sender=request.user, recipient=recipient,
                          subject=request.POST['subject'], body=request.POST['body'])
        message.save()
        return redirect('inbox')
    else:
        return render(request, 'messaging/compose.html')


@login_required
def view_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    if message.recipient == request.user:
        message.read_at = timezone.now()
        message.save()
    return render(request, 'messaging/view_message.html', {'message': message})
