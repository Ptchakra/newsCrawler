from django import forms
from .models import TrangWeb


class AddTargetForm(forms.Form):
    ten_trang_web = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-them-trang-web",
                "id": "domainName",
                "placeholder": "example.com"
            }
        ))
    vung_tin_tuc = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-them-trang-web",
                "id": "vungThemTrangWeb",
            }
        ))
    domain_description = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-them-trang-web",
                "id": "domainDescription",
            }
        ))


class UpdateTargetForm(forms.ModelForm):
    class Meta:
        fields = ['domain_name', 'domain_description']
    domain_name = forms.CharField(
        required=True,
        disabled=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "domainName",
            }
        ))
    domain_description = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "domainDescription",
            }
        ))

    def set_value(self, domain_value, domain_description_value):
        self.initial['domain_name'] = domain_value
        self.initial['domain_description'] = domain_description_value
