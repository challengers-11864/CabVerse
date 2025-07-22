from django.contrib import admin
from . models import *
admin.site.register(Rider)
admin.site.register(Driver)
admin.site.register(Ride)
admin.site.register(DriverRating)
admin.site.register(RiderRating)
