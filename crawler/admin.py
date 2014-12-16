from django.contrib import admin
from crawler.models import Destination
# Register your models here.



def search_destination(modeladmin, request, queryset):
    pass

search_destination.short_description = "Search destination"


class DestinationAdmin(admin.ModelAdmin):
    search_fields = ('name', 'path')
    list_filter = ('name', 'path')
    list_display = ('name', 'path')
    actions = [search_destination]


admin.site.register(Destination, DestinationAdmin)
