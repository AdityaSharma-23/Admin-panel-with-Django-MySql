from django .forms import ModelForm
from .models import schedular

class schedularForm(ModelForm):
    class Meta:
        model = schedular
        fields = '__all__'