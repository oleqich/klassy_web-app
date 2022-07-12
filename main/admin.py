from django.contrib import admin
from .models import ReserveModel
from .models import ChefsModel, DishesModel

# Register your models here.
admin.site.register(ReserveModel)
admin.site.register(ChefsModel)
admin.site.register(DishesModel)

