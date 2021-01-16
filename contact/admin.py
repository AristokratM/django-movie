from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'date')


admin.site.register(Contact, ContactAdmin)