from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReserveForm

# Create your views here.

def reserve(request):
    error = ''
    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Invalid form'
    form = ReserveForm()

    data = {
        'form':form,
        'error':error
    }

    return render(request, 'main/index.html', data)

# Create your views here.
def index(request):
    return reserve(request)
