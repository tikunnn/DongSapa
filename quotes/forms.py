from django import forms
from .models import Company, Contract, Customer


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['quote_number', 'created_by', 'team_leader', 'sales_rep',
                  'customer_source', 'customer_source_type', 'quote_type']
        labels = {
            'quote_number': 'Số báo giá',
            'created_by': 'Người lập báo giá',
            'team_leader': 'Trưởng nhóm',
            'sales_rep': 'Đại diện bán hàng',
            'customer_source': 'Nguồn khách hàng',
            'customer_source_type': 'Loại nguồn khách hàng',
            'quote_type': 'Loại báo giá',
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['company_name', 'contact_person', 'phone_number', 'address']
        labels = {
            'company_name': 'Tên công ty',
            'contact_person': 'Người liên hệ',
            'phone_number': 'Số điện thoại',
            'address': 'Địa chỉ',
        }


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['project_name', 'bid_package', 'project_address', 'construction_items',
                  'brand_name', 'airCondition_type', 'construction_type', 'project_type', 'region']
        labels = {
            'project_name': 'Tên công trình',
            'bid_package': 'Gói thầu',
            'project_address': 'Địa chỉ công trình',
            'construction_items': 'Mặt hàng thi công',
            'brand_name': 'Tên thương hiệu',
            'airCondition_type': 'Loại điều hòa',
            'construction_type': 'Loại công trình',
            'project_type': 'Loại dự án',
            'region': 'Khu vực',
        }
