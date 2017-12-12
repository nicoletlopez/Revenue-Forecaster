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



    #earliest_date = min(Actual.objects.values_list('date',flat='true')).strftime('%Y-%m-%d')
    #latest_date = max(Actual.objects.values_list('date',flat='true')).strftime('%Y-%m-%d')

    earliest_date = '2015-01-31'
    latest_date = '2016-12-31'

    metric = forms.MultipleChoiceField(choices=METRIC_CHOICE,initial='rev')
    start_date = forms.DateField(input_formats=['%Y-%m-%d'],initial=earliest_date,widget=widgets.AdminDateWidget())
    end_date = forms.DateField(input_formats=['%Y-%m-%d'],initial=latest_date,widget=widgets.AdminDateWidget())
    number_of_predictions = forms.IntegerField(initial=1)
    season_length = forms.IntegerField(initial=12)
    fitting_method=forms.ChoiceField(widget=forms.RadioSelect,choices=FITTING_METHOD,initial='sse')

    alpha = forms.FloatField(max_value=1.0,min_value=0.01,required=False)
    beta = forms.FloatField(max_value=1.0,min_value=0.01,required=False)
    gamma = forms.FloatField(max_value=1.0, min_value=0.01,required=False)

    #may have errors if constant_value_end is greater than constant_value_start
    constant_value_start = forms.FloatField(max_value=1,min_value=100,required=False)
    constant_value_end = forms.FloatField(max_value=1,min_value=100,required=False)
    constant_value_step = forms.FloatField(max_value=10,min_value=1,required=False)

#class XlToDbForm(forms.Form):
#    year=forms.IntegerField(max_value=2016,min_value=2014,initial=2015)
#    file=forms.ModelChoiceField(queryset=Project.objects.all().filter())
