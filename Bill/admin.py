from django.contrib import admin
from .models import Bill

# Register your models here.
class BillAdmin(admin.ModelAdmin):
    list_display = ['supplier_name', 'bill_value']
    
admin.site.register(Bill, BillAdmin)

