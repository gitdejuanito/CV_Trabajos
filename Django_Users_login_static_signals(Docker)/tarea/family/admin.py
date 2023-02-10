from django.contrib import admin
from family.models import familia
# Register your models here.


#-->Sirve para mostrar esta info en el display de admin
class familiaAdmin(admin.ModelAdmin):
    list_display=("equipo", "liga")
    search_fields=("equipo","liga",)

admin.site.register(familia, familiaAdmin)