from django.contrib import admin
from accounts.models import Person

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    model = Person

admin.site.register(Person, PersonAdmin)
