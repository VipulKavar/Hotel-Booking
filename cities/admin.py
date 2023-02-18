from django.contrib import admin

from cities.models import City


# Register your models here.
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'country',)
    list_filter = ('state',)
    search_fields = ('name', 'state',)


admin.site.register(City, CityAdmin)
