from django.contrib import admin
from .models import Clas, Club, Reservation

@admin.action(description='Make selected classes unreserved')
def make_free(modeladmin, request, queryset):
    for i in queryset:
        Reservation.objects.all().filter(clas=i.id).delete()

class ClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'capacity', 'status']
    ordering = ['name']
    actions = [make_free]
    def status(self, obj):
        if hasattr(obj, 'reservation'):
            return 'Reserved'
        else:
            return 'Unreserved'

# Register your models here.
admin.site.register(Club)
admin.site.register(Reservation)
admin.site.register(Clas, ClassAdmin)

