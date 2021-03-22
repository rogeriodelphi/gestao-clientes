from django.shortcuts import render, redirect
from django.contrib.auth import logout

# TODO: Refatorar para usar Threads assim que possível
def home(request):
    return render(request, 'home.html')

# FIXME: Corrigir BUG ....
def my_logout(request):
    logout(request)
    return redirect('home')
