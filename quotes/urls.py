from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateDataView.as_view(), name='quote')
]
