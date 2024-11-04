from django import forms
from crudapp.models import employee

class employeeform(forms.ModelForm):
    class Meta:
        model = employee
        fields = '__all__'  # Includes all fields from the model in the form


# used to create form based on model , ( by using form , user can able to enter data).
