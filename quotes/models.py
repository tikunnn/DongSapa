from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    quote_number = models.CharField(max_length=50, unique=True)
    created_by = models.CharField(max_length=255)
    team_leader = models.CharField(max_length=255)
    sales_rep = models.CharField(max_length=255)
    customer_source = models.CharField(max_length=100)
    customer_source_type = models.CharField(max_length=50)
    quote_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Số báo giá: {self.quote_number}"


class Customer(models.Model):
    company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name


class Contract(models.Model):
    project_name = models.CharField(max_length=255)
    bid_package = models.CharField(max_length=50)
    project_address = models.CharField(max_length=255)
    construction_items = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=50)
    airCondition_type = models.CharField(max_length=50)
    construction_type = models.CharField(max_length=50)
    project_type = models.CharField(max_length=50)
    region = models.CharField(max_length=100)

    # company = models.ForeignKey(Company, related_name='contracts', on_delete=models.CASCADE)

    def __str__(self):
        return f"Tên công trình: {self.project_name} tại {self.region}"


class RequestPrice(models.Model):
    name_product = models.CharField(max_length=255)
    id_product = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return self.name_product


# class Employee(models.Model):
#     name = models.CharField(max_length=255, verbose_name='Tên nhân viên')
#     position = models.CharField(max_length=100, verbose_name='Chức vụ')
#     team_leader = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='team_members', verbose_name='Trưởng Team')
#     company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees', verbose_name='Công ty')

#     def __str__(self):
#         return self.name

#     def get_team_leader(self):
#         return self.team_leader.name if self.team_leader else 'Không có leader'


# Notes:
# Tạo và áo dụng Migrations:

# python manage.py makemigrations
# python manage.py migrate
