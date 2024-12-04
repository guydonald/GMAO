from django.contrib import admin
from .models import OrderWork, Intervention, PieceUtilisee

# Register your models here.
admin.site.register(OrderWork)
admin.site.register(Intervention)
admin.site.register(PieceUtilisee)