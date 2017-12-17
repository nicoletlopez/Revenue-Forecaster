from django.contrib.auth.models import User
from django import forms
#from django.db import models
#from django.forms import ModelForm
from django.contrib.admin import widgets
from datetime import datetime
from .models import Project,File, Actual
#choice fields for the ForecastOptionsForm class
METRIC_CHOICE = \
    (
        ('rev','Revenue'),
        ('arr','Average Room Rate'),
        ('ocr','Occupancy Rate'),
        ('revpar','Revenue per Available Room')
    )
FITTING_METHOD = \
    (
        ('mse','MSE (Mean Squared Errors)'),
        ('sse','SSE (Sum of Squared Errors)'),
        ('mad','MAD (Mean Absolute Deviation)')
    )

FORECAST_SUB_SEGMENT = \
    (
        ('TOTAL','Total Individual and Group'),
        ('IND','Total Individual'),
        ('GRP','Total Group'),
        ('RCK','Rack'),
        ('CORP','Corporate'),
        ('CORPO','Corporate Others'),
        ('PKG/PRM','Packages/Promo'),
        ('WSOL','Wholesale Online'),
        ('WSOF','Wholesale Offline'),
        ('INDO','Individual Others'),
        ('INDR','Industry Rate'),

        ('CORPM','Corporate Meetings'),
        ('CON/ASSOC','Convention/Association'),
        ('GOV\'T/NGOS','Government/NGO'),
        ('GRPT','Group Tours'),
        ('GRPO','Group Others'),
    )

SEGMENTS = \
(
    ('RCK', 'Rack'),
    ('CORP', 'Corporate'),
    ('CORPO', 'Corporate Others'),
    ('PKG/PRM', 'Packages/Promo'),
    ('WSOL', 'Wholesale Online'),
    ('WSOF', 'Wholesale Offline'),
    ('INDO', 'Individual Others'),
    ('INDR', 'Industry Rate'),
    ('CORPM', 'Corporate Meetings'),
    ('CON/ASSOC', 'Convention/Association'),
    ('GOV\'T/NGOS', 'Government/NGO'),
    ('GRPT', 'Group Tours'),
    ('GRPO', 'Group Others'),
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

    #by sub/segment
    segment = forms.ChoiceField(choices=FORECAST_SUB_SEGMENT, initial='Total Individual and Group')
    """alpha = forms.FloatField(max_value=1.0,min_value=0.01,required=False,initial=0.6)
    beta = forms.FloatField(max_value=1.0,min_value=0.01,required=False,initial=0.4)
    gamma = forms.FloatField(max_value=1.0, min_value=0.01,required=False,initial=0.5)

    #may have errors if constant_value_end is greater than constant_value_start
    constant_value_start = forms.FloatField(min_value=1,max_value=101,required=False,initial=1)
    constant_value_end = forms.FloatField(min_value=1,max_value=101,required=False,initial=101)
    constant_value_step = forms.FloatField(min_value=1,max_value=9,required=False,initial=9)"""

#this is just a workaround
class CustomForecastForm(forms.Form):
    #earliest_date = min(Actual.objects.values_list('date',flat='true')).strftime('%Y-%m-%d')
    #latest_date = max(Actual.objects.values_list('date',flat='true')).strftime('%Y-%m-%d')

    earliest_date = '2015-01-31'
    latest_date = '2016-12-31'

    metric = forms.MultipleChoiceField(choices=METRIC_CHOICE,initial='rev')
    start_date = forms.DateField(input_formats=['%Y-%m-%d'],initial=earliest_date,widget=widgets.AdminDateWidget())
    end_date = forms.DateField(input_formats=['%Y-%m-%d'],initial=latest_date,widget=widgets.AdminDateWidget())
    number_of_predictions = forms.IntegerField(initial=1)
    season_length = forms.IntegerField(initial=12)
    #fitting_method=forms.ChoiceField(widget=forms.RadioSelect,choices=FITTING_METHOD,initial='sse')

    alpha = forms.FloatField(max_value=1.0,min_value=0.01,required=False,initial=0.6)
    beta = forms.FloatField(max_value=1.0,min_value=0.01,required=False,initial=0.4)
    gamma = forms.FloatField(max_value=1.0, min_value=0.01,required=False,initial=0.5)

    #may have errors if constant_value_end is greater than constant_value_start
    constant_value_start = forms.FloatField(min_value=1,max_value=101,required=False,initial=1)
    constant_value_end = forms.FloatField(min_value=1,max_value=101,required=False,initial=101)
    constant_value_step = forms.FloatField(min_value=1,max_value=9,required=False,initial=9)

class UpdateRnaForm(forms.Form):

    segment = forms.ChoiceField(initial="RACK", choices=SEGMENTS)
    date = forms.DateField(initial='2015-01-31')
    rna = forms.FloatField()



#class XlToDbForm(forms.Form):
#    year=forms.IntegerField(max_value=2016,min_value=2014,initial=2015)
#    file=forms.ModelChoiceField(queryset=Project.objects.all().filter())
