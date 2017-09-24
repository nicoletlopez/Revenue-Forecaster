from django.views import generic
from django.views.generic import View,TemplateView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.core.urlresolvers import reverse_lazy
from .forms import UserForm
from .models import Project,File

def StartView(request):
    return redirect('rfs:login')

def LoginView(request):
    template_name='rfs/login.html'
    return render(request,template_name)

def IndexView(request):

    projects=Project.objects.all()
    context={'all_projects':projects}
    template_name='rfs/base.html'
    return render(request,template_name,context)

#PROJECT VIEWS
class ProjectDetail(DetailView):
    model=Project
    template_name='rfs/project.html'

    def get_context_data(self,**kwargs):
        context=super(ProjectDetail,self).get_context_data(**kwargs)
        context['all_projects']=Project.objects.all()
        context['all_files']=File.objects.all()
        return context

class ProjectCreate(CreateView):
    model=Project
    template_name='rfs/project_create.html'
    fields=['project_name','description']
    def get_context_data(self,**kwargs):
        context=super(ProjectCreate,self).get_context_data(**kwargs)
        context['all_projects']=Project.objects.all()
        return context

class FileAdd(TemplateView):
    model=File
    template_name='rfs/file_add.html'
    fields=['file_name']

    def get_context_data(self,**kwargs):
        context=super(FileAdd,self).get_context_data(**kwargs)
        context['all_projects']=Project.objects.all()
        context['all_files'] = File.objects.all()
        return context
