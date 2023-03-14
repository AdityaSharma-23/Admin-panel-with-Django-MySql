from django.db.models import fields
import django_filters
from django_filters import CharFilter


from .models import *

class schedularFilter(django_filters.FilterSet):
    Staff_Email_ID = CharFilter(field_name="staff_email_id", lookup_expr='icontains', label='Staff-Email-ID')

    class Meta:
        model = schedular
        fields = '__all__'
        exclude = ['staff_email_id'] 

        