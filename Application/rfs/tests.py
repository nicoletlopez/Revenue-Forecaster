from django.views import generic
from django.views.generic import View,TemplateView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy,reverse
from .forms import UserForm,FileForm,CreateForm
from .models import Project,File, Actual, Forecast, Seg_list
from django.http import HttpResponse,Http404,HttpResponseRedirect
from os.path import join, dirname, abspath
import datetime, xlrd,numpy as np
from xlrd.sheet import ctype_text

def test(request):
    return render(request,'rfs/data_table.html')
