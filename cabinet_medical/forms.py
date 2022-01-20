from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



from .models import *

class RdvForm(ModelForm):
    class Meta:
        model = RDV
        fields = "__all__"


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"


