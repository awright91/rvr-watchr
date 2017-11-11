from django.contrib import admin
from river_subs.models import RiverSubscription
# Register your models here.


class SubAdmin(admin.ModelAdmin):
    list_display = ('user', 'river')



admin.site.register(RiverSubscription, SubAdmin)
