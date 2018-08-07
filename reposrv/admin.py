from django.contrib import admin

# Register your models here.
from .models import Customer, Address, Blockchain, Watchlist, Log, Operations
admin.site.register(Customer)
#admin.site.register(Address)
admin.site.register(Blockchain)
#admin.site.register(Watchlist)
admin.site.register(Log)
admin.site.register(Operations)

# Define the admin class
class AddressAdmin(admin.ModelAdmin):
    list_display = ('key', 'display_customer','display_blockchain', 'addrstatus')

# Register the admin class with the associated model
admin.site.register(Address, AddressAdmin)

# Define the admin class
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('address','startdate','completedate','result','status')

# Register the admin class with the associated model
admin.site.register(Watchlist, WatchlistAdmin)


