from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


def home(request):
  records = Record.objects.all()
  # Check if user is logging in
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    # Authenticate
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, "You have successfully logged in.")
      return redirect('home')
    else:
      messages.error(request, "Invalid username or password.")
      return redirect('home')
  return render(request, 'home.html', {'records': records})

def logout_user(request):
  logout(request)
  messages.success(request, "You have successfully logged out.")
  return redirect('home')

def register_user(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      # Authenticate and login
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=password)
      login(request, user)
      messages.success(request, "You have successfully registered.")
      return redirect('home')
  else:
    form = SignUpForm()
    return render(request, 'register.html', {'form': form})
  return render(request, 'register.html', {'form': form})

def customer_record(request, pk):
  if request.user.is_authenticated:
    # Lookup records
    record = Record.objects.get(id=pk)
    return render(request, 'record.html', {'record': record})
  else:
    messages.error(request, "You must be logged in to view records.")
    return redirect('home')

def delete_record(request, pk):
  if request.user.is_authenticated:
    record_to_delete = Record.objects.get(id=pk)
    record_to_delete.delete()
    messages.success(request, "Record deleted Successfully.")
    return redirect('home')
  else:
    messages.error(request, "You must be logged in to delete records.")
    return redirect('home')

def add_record(request):
  if request.user.is_authenticated:
    form = AddRecordForm(request.POST or None)
    if request.method == "POST":
      if form.is_valid():
        form.save()
        messages.success(request, "Record added Successfully.")
        return redirect('home')
    return render(request, 'add_record.html', {'form':form})
  else:
    messages.error(request, "You must be logged in to add a record.")
    return redirect('home')

def update_record(request, pk):
  if request.user.is_authenticated:
    current_record = Record.objects.get(id=pk)
    form = AddRecordForm(request.POST or None, instance=current_record)
    if form.is_valid():
      form.save()
      messages.success(request, "Record updated Successfully.")
      return redirect('home')
    return render(request, 'update_record.html', {"form":form})
  else:
    messages.error(request, "You must be logged in to update a record.")
    return redirect('home')