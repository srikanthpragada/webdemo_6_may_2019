from django import forms

from .models import Employee


class AddJobForm(forms.Form):
    title = forms.CharField(max_length=30)
    minsal = forms.IntegerField(required=False)
    maxsal = forms.IntegerField(required=False)


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee  # Model on which form is built
        fields = ['fullname', 'title', 'salary']  # Fields to be included
