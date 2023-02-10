from django.contrib import admin
from Users.models import customer
# Register your models here.

@admin.register(customer)
class customerAdmin(admin.ModelAdmin):
    list_display=("Username", "name",)
    search_fields=("Username","name",)

