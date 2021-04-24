from django import forms
from .models import TrangWeb

defaulWidthHtml = "width : 500px"

class AddTargetForm(forms.Form):
    link_trang_web = forms.CharField(
        required=True,
        label='Link trang web',
        widget=forms.TextInput(
            attrs={
                "class": "form-them-trang-web",
                "id": "domainName",
                "placeholder": "https://example.com/thoi-su",
                "style" : defaulWidthHtml,
            }
        ))
    the_vung_tin_tuc = forms.CharField(
        required=True,
        label='Thẻ vùng tin tức',
        widget=forms.TextInput(
            attrs={
                "class": "form-them-trang-web",
                "id": "vungThemTrangWeb",
                "placeholder": "<body class='page-folder ' data-source='Folder'>",
                "style" : defaulWidthHtml,
            }
        ))
    thu_tu_cua_the_vung_tin_tuc = forms.IntegerField(
        required=False,
        label='Thứ tự thẻ vùng tin tức',
        widget=forms.TextInput(
            attrs={
                "class": "form-them-trang-web",
                "id": "domainDescription",
                "style" : defaulWidthHtml,
                "value" : 1,
            }
        ))
    the_tieu_de = forms.CharField(
        required=True,
        label="Thẻ tiêu đề",
        widget=forms.TextInput(
            attrs={
                "class": "form-them-trang-web",
                "id": "vungThemTrangWeb",
                "placeholder": "<body class='page-folder ' data-source='Folder'>",
                "style" : defaulWidthHtml,
            }
        ))
    thu_tu_cua_the_tieu_de = forms.IntegerField(
        required=False,
        label="Thứ tự thẻ tiêu đề",
        widget=forms.TextInput(
            attrs={
                "class": "form-them-trang-web",
                "id": "domainDescription",
                "style" : defaulWidthHtml,
                "value" : 1,
                
            }
        ))
    the_noi_dung = forms.CharField(
        required=True,
        label="Thẻ nội dung",
        widget=forms.TextInput(
            attrs={
                "class": "form-them-trang-web",
                "id": "vungThemTrangWeb",
                "placeholder": "<body class='page-folder ' data-source='Folder'>",
                "style" : defaulWidthHtml,
            }
        ))
    thu_tu_the_noi_dung = forms.IntegerField(
        required=False,
        label="Thứ tự thẻ nội dung",
        widget=forms.TextInput(
            attrs={
                "class": "form-them-trang-web",
                "id": "domainDescription",
                "style" : defaulWidthHtml,
                "value" : 1,
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
