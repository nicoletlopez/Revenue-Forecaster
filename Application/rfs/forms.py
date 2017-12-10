from django.contrib.auth.models import User
from django import forms
from .models import Project,File, Actual
from django.contrib.admin import widgets
from datetime import datetime
#choice fields for the ForecastOptionsForm class
METRIC_CHOICE = \
    (
        ('rev','Revenue'),
        ('arr','Average Room Rate'),
        ('occ','Occupancy Rate'),
        ('revpar','Revenue per Available Room')
    )
FITTING_METHOD = \
    (
        ('mse','MSE (Mean Squared Error)'),
        ('sse','SSE (Sum of Squared Error)'),
        ('mad','MAD (Mean Absolute Deviation')
    )

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','password']

class FileForm(forms.ModelForm):

    class Meta:
        model=File
        fields=['excel_file']

class CreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.fields['project_name'].widget.attrs = {'class': 'form-control'}
        self.fields['description'].widget.attrs = {'class': 'form-control'}

    class Meta:
        model=Project
        fields=['project_name','description']

class ForecastOptionsForm(forms.Form):

    earliest_date = min(Actual.objects.values_list('date'))
    latest_date = max(Actual.objects.values_list('date'))

    metric = forms.MultipleChoiceField(choices=METRIC_CHOICE)

    start_date = forms.DateTimeField(input_formats=['%Y-%m-%d'],show_hidden_initial=earliest_date,widget=widgets.AdminDateWidget())
    end_date = forms.DateField(input_formats=['%Y-%m-%d'],widget=widgets.AdminDateWidget())
    n_preds = forms.IntegerField()
    smoothing_method=forms.RadioSelect(choices=FITTING_METHOD)

#class XlToDbForm(forms.Form):
#    year=forms.IntegerField(max_value=2016,min_value=2014,initial=2015)
#    file=forms.ModelChoiceField(queryset=Project.objects.all().filter())
