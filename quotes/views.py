from django.shortcuts import render
from django.contrib import messages
from django.views import View
from .forms import CompanyForm, CustomerForm, ContractForm


# Create your views here.
class CreateDataView(View):
    def get(self, request, *args, **kwargs):
        company_form = CompanyForm()
        customer_form = CustomerForm()
        contract_form = ContractForm()

        return render(request, 'quotes/quote.html', {
            'company_form': company_form,
            'customer_form': customer_form,
            'contract_form': contract_form,
        })

    def post(self, request, *args, **kwargs):
        company_form = CompanyForm(request.POST)
        customer_form = CustomerForm(request.POST)
        contract_form = ContractForm(request.POST)

        if company_form.is_valid() and customer_form.is_valid() and contract_form.is_valid():
            company_form.save()
            customer_form.save()
            contract_form.save()

            messages.success(request, "Dữ liệu đã được lưu thành công!")
            return render(request, 'quotes/quote.html', {
                'company_form': company_form,
                'customer_form': customer_form,
                'contract_form': contract_form,
            })
        else:
            messages.error(request, "Vui lòng kiểm tra lại thông tin.")
            return render(request, 'quotes/quote.html', {
                'company_form': company_form,
                'customer_form': customer_form,
                'contract_form': contract_form,
            })

        # return render(request, self.template_name, {
        #     'company_form': company_form,
        #     'customer_form': customer_form,
        #     'contract_form': contract_form
        # })
