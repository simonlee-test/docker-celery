from django.contrib import admin
from .models import Food

# Register your models here.
class FoodAdmin(admin.ModelAdmin):
    list_display=("pk", "name")
    
admin.site.register(Food, FoodAdmin)