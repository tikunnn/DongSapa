from django.contrib import admin
from .models import Company, Contract, Customer

# Register your models here.
admin.site.register(Company)
admin.site.register(Customer)
admin.site.register(Contract)
