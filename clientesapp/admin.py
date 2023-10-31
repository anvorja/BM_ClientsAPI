from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Client, ClientAdmin)
