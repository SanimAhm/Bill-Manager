from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView
from .models import *
from django.urls import reverse_lazy
from .forms import *
from django.db.models import Sum, Q, Case, When, IntegerField
import pandas as pd

# Create your views here.
class BillView(ListView):
    model = Bill
    template_name = 'home.html'
    context_object_name = 'bill'

    def get_queryset(self):
        queryset = Bill.objects.all()  # start with all bills
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(supplier_name__icontains=q)  # filter by supplier name
        
        # Custom ordering: Pending -> Received -> Paid
        queryset = queryset.annotate(
            status_order=Case(
                When(status='Pending', then=0),
                When(status='Signed', then=1),
                When(status='Received', then=2),
                When(status='Paid', then=3),
                default=4,
                output_field=IntegerField()
            )
        ).order_by('status_order', 'receive_date')  # secondary ordering by date
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pending_bills = Bill.objects.filter(status='Pending')
        context['pending_count'] = pending_bills.count()
        context['pending_value'] = pending_bills.aggregate(total_value=Sum('bill_value'))['total_value'] or 0
        context['search_query'] = self.request.GET.get('q', '')
        return context

class BillDetailView(DetailView):
    model = Bill
    template_name = "bill_detail.html"
    

def success(request):
    return render(request, "success.html")

class BillRegister(CreateView):
    model = Bill
    form_class = BillForm
    template_name = 'bill_register.html'
    success_url = reverse_lazy('success')
    