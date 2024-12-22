from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from . forms import signUpForm, addRecordForm
from .models import Records




def home(request):  
    records = Records.objects.all() 
    
    
    # Pastikan pengguna sudah login
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']
        
        # Autentikasi pengguna
        user = authenticate(request, username=username, password=password)
        # Login
        if user is not None :
            login(request, user)
            messages.success(request, 'Berhasil Login')
            return redirect('home')
        else :
            messages.error(request, 'Gagal Login')
            return redirect('home')
    
    context = {
        "records"   : records
    }
    return render(request, 'home.html', context)    

def logoutUser(request):
    logout(request)
    messages.success(request, 'Berhasil Logout')
    return redirect('home')

def registerUser(request):
    if request.method == "POST" :
        form = signUpForm(request.POST)
        
        if form.is_valid() :
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Berhasil Register')
            return redirect('home')
    else :
        context = {
            'form': signUpForm()
        }
        return render(request, 'register.html', context)
    context = {
        'form': signUpForm()
    }
    return render(request, 'register.html', context)

def customerRecord(request, pk):
    if request.user.is_authenticated :
        customerRecord = Records.objects.get(id=pk)
        context = {
            'customer': customerRecord
        }
        return render(request, 'record.html', context)
    else :
        messages.error(request, 'Silahkan login terlebih dahulu')  
        return redirect('home')

def deleteRecord(request, pk):
    if request.user.is_authenticated :
        record = Records.objects.get(id=pk)
        record.delete()
        messages.success(request, 'Data berhasil dihapus')
        return redirect('home')
    else :
        messages.error(request, 'Silahkan login terlebih dahulu')  
        return redirect('home')

def addRecord(request):
    form    = addRecordForm(request.POST or None)
    if request.user.is_authenticated :
        if request.method == "POST" :
            if form.is_valid() :
                form.save()
                messages.success(request, 'Data berhasil ditambahkan')
                return redirect('home')
        context = {
            'form': addRecordForm()
        }
        return render(request, 'add_record.html', context)
    else :
        messages.error(request, 'Silahkan login terlebih dahulu')  
        return redirect('home')

def updateRecord(request, pk):
    if request.user.is_authenticated :
        record = Records.objects.get(id=pk)
        form = addRecordForm(instance=record)
        if request.method == "POST" :
            form = addRecordForm(request.POST, instance=record)
            if form.is_valid() :
                form.save()
                messages.success(request, 'Data berhasil diupdate')
                return redirect('home')
        context = {
            'form': form,
            'pk'    : pk
        }
        return render(request, 'add_record.html', context)




