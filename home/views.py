from django.shortcuts import render, redirect
from django.contrib.auth import logout

def calcular(v1, v2):
    return v1/v2

# TODO: Refatorar para usar Threads assim que possível
def home(request):
    # import pdb; pdb.set_trace()
    value1 = 10
    value2 = 20
    res = calcular(value1, value2)
    return render(request, 'home.html', {'result': res})

# FIXME: Corrigir BUG ....
def my_logout(request):
    logout(request)
    return redirect('home')
