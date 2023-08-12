from django.contrib import admin
from .models import Carpinteros, Electricistas, Plomeros, Gasistas, Pintores, Avatar

# Register your models here.

admin.site.register(Carpinteros)
admin.site.register(Electricistas)
admin.site.register(Plomeros)
admin.site.register(Gasistas)
admin.site.register(Pintores)
admin.site.register(Avatar)
