from django.contrib import admin
from arboles.models import Arbol, Censista
# Register your models here.

class ArbolAdmin(admin.ModelAdmin):
    # ...
    list_display = ('especie', 'pub_date')

admin.site.register(Arbol, ArbolAdmin)
admin.site.register(Censista)
