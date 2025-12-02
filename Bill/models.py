from django.db import models

# Create your models here.
class Bill(models.Model):
    
    STATUS_CHOICE = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('Signed', 'Signed'),
        ('Received', 'Received')
    ]
    UNIT_CHOICE = [
        ('Flour Mill', 'Flour Mill'),
        ('Drinking Water', 'Drinking Water'),
        ('FM & DW', 'FM & DW')
    ]
    
    receive_date = models.DateField(null=False, blank=False)
    supplier_name = models.CharField(max_length=200, null=False, blank=False)
    unit = models.CharField(max_length=20, choices=UNIT_CHOICE)
    bill_no = models.CharField(max_length=50)
    invoice_no = models.CharField(max_length=50)
    bill_value = models.DecimalField(max_digits=20, decimal_places=2)
    tds = models.DecimalField(max_digits=20, decimal_places=2)
    vds = models.DecimalField(max_digits=20, decimal_places=2)
    net_payment = models.DecimalField(max_digits=20, decimal_places=2)    
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default='Received', null=False, blank=False)
    payment_date = models.DateField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    
    class Meta:
        ordering = ['-status']
        
    def __str__(self):
        return self.supplier_name