from domain.aggregates import Bill
from django import forms


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = "__all__"
