from django.contrib import admin
from .models import BandMember, Album, Concert

# Register models in Django's admin panel for easy management.
admin.site.register(BandMember)
admin.site.register(Album)
admin.site.register(Concert)


print()
