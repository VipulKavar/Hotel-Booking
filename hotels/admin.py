from django.contrib import admin

from hotels.models import Hotel, Feature, HotelImage


# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager', 'city', 'rating', 'price',)
    list_filter = ('rating', 'city',)
    search_fields = ('name', 'city', 'manager')


admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelImage)
admin.site.register(Feature)
