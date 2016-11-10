from django import forms
from django.utils.safestring import mark_safe


class BusinessForm(forms.Form):
    business_type = forms.CharField(label="Business Type", max_length=200)
    businees_name = forms.CharField(label="Name", max_length=200)
    business_address = forms.CharField(label="Address", max_length=200)
    businees_telephone = forms.CharField(label="Telephone", max_length=11)
    businees_fax = forms.CharField(label="Fax", max_length=11)
    businees_email = forms.CharField(label="email", max_length=200)