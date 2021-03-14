from django import forms
from .models import TrangWeb


class AddTargetForm(forms.Form):
    link_trang_web = forms.CharField(
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
    thu_tu_vung_tin_tuc = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-them-trang-web",
                "id": "domainDescription",
            }
        ))
    the_tieu_de = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-them-trang-web",
                "id": "vungThemTrangWeb",
            }
        ))
    thu_tu_the_tieu_de = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-them-trang-web",
                "id": "domainDescription",
            }
        ))
    the_noi_dung = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-them-trang-web",
                "id": "vungThemTrangWeb",
            }
        ))
    thu_tu_the_noi_dung = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-them-trang-web",
                "id": "domainDescription",
            }
        ))


class UpdateTargetForm(forms.ModelForm):
    class Meta:
        fields = ['link_trang_web', 'vung_tin_tuc', 'vung_tin_tuc', 'thu_tu_vung_tin_tuc', 'the_tieu_de', 'thu_tu_the_tieu_de', 'the_noi_dung', 'thu_tu_the_noi_dung']
    link_trang_web = forms.CharField(
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
    thu_tu_vung_tin_tuc = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-them-trang-web",
                "id": "domainDescription",
            }
        ))
    the_tieu_de = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-them-trang-web",
                "id": "vungThemTrangWeb",
            }
        ))
    thu_tu_the_tieu_de = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-them-trang-web",
                "id": "domainDescription",
            }
        ))
    the_noi_dung = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-them-trang-web",
                "id": "vungThemTrangWeb",
            }
        ))
    thu_tu_the_noi_dung = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-them-trang-web",
                "id": "domainDescription",
            }
        ))

    def set_value(self, domain_value, domain_description_value):
        self.initial['domain_name'] = domain_value
        self.initial['domain_description'] = domain_description_value
