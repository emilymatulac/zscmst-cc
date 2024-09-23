from django.contrib import admin
from .models import CitizenCharter
from .models import TableProcess
from .models import TableOffice

# # Register your models here.
admin.site.register(CitizenCharter)
admin.site.register(TableProcess)
admin.site.register(TableOffice)

