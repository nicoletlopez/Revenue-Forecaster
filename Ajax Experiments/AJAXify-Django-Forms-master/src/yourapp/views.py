from django.shortcuts import render
from django.views.generic import FormView

from .forms import JoinForm
from .mixins import AjaxFormMixin

class JoinFormView(FormView):
    form_class = JoinForm
    template_name  = 'forms/ajax.html'
    success_url = '/form-success/'
