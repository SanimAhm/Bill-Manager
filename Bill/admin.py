from django.contrib import admin
from .models import Bill

# Register your models here.
class BillAdmin(admin.ModelAdmin):
    list_display = ['supplier_name', 'bill_value', 'net_payment', 'status']
    search_fields = ['supplier_name']
    list_filter = ['status', 'receive_date']
    
admin.site.register(Bill, BillAdmin)

