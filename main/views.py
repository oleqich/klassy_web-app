from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from .forms import ReserveForm
from .models import ChefsModel, DishesModel

# Create your views here.

def reserve(request):
    chefs = ChefsModel.objects.all()
    dishes = DishesModel.objects.all()
    error = ''
    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Invalid form'
    else:
        form = ReserveForm()

    return render(request, 'main/index.html', {'form':form, 'error':error, 'chefs':chefs, 'dishes':dishes, })

# Create your views here.
def index(request):
    return reserve(request)
