from django.shortcuts import render
from .forms import ReserveForm

# Create your views here.

def reserve(request):
    error = ''
    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Invalid form'
    form = ReserveForm()

    data = {
        'form':form,
        'error':error
    }

    return render(request, 'main/index.html', data)