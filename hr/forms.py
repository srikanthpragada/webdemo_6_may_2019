from django import forms


class AddJobForm(forms.Form):
    title = forms.CharField(max_length=30)
    minsal = forms.IntegerField(required=False)
    maxsal = forms.IntegerField(required=False)

