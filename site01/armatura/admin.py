from django.contrib import admin
from .models import *

# Register your models here.

class sortam_armaturaAdmin(admin.ModelAdmin):
    list_display = ["Dim", "Ves", "Plosh"]


class Meta:
    model = sortam_armatura

admin.site.register(sortam_armatura, sortam_armaturaAdmin)
#admin.site.register(armatura)