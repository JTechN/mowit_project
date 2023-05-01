from django.forms import ModelForm
from Contractor.models import Service, RequestService
from django import forms



# class ServiceForm(ModelForm):
  # name = ModelForm.CharField(max_length=200, null=True)
  # price = forms.FloatField(null=True)
  # description = forms.CharField(max_length=200, null=True)
  # class Meta:
  #   model = Service
  #   fields = ("name", "price", "description", "tags")




class ServiceForm(forms.ModelForm):

  class Meta:
    model = Service
    fields = ("account", "name", "price", "description", "tags")

  def save(self, commit=True):
        service = super(ServiceForm, self).save(commit=False)

        if commit:
            service.save()
        return service
  
class RequestServiceForm(forms.ModelForm):
    class Meta:
        model = RequestService
        fields = ('customer', 'contractor', 'service')


class RequestServiceUpdateForm(forms.ModelForm):
    STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Out for Service', 'Out for Service'),
    ('Completed', 'Completed'),
    )

    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True)

    class Meta:
        model = RequestService
        fields = ('customer', 'contractor', 'service', 'status')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the initial values of the fields based on the values in the database
        instance = kwargs.get('instance')
        if instance:
            self.initial['customer'] = instance.customer
            self.initial['contractor'] = instance.contractor
            self.initial['service'] = instance.service

