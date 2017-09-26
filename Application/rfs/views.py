from django.views import generic
from django.views.generic import View,TemplateView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from django.core.urlresolvers import reverse_lazy
from .forms import UserForm,FileForm
from .models import Project,File


EXCEL_FILE_TYPES=['xlsx','xls']

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

class ProjectDelete(DeleteView):
    model=Project
    success_url=reverse_lazy('rfs:index')

def FileAdd(request,project_id):
    form=FileForm(request.POST or None,request.FILES or None)
    project=get_object_or_404(Project,pk=project_id)
    projects=Project.objects.all()

    if form.is_valid():
        project_files = project.file_set.all()
        for f in project_files:
            if f.excel_file == form.cleaned_data.get("excel_file"):
                context = {
                    'all_projects':projects,
                    'all_files': File.objects.all(),
                    'project': project,
                    'form': form,
                    'error_message': 'You already added that file',
                }
                return render(request, 'rfs/file_add.html', context)
        file = form.save(commit=False)
        file.project = project
        file.excel_file = request.FILES['excel_file']
        file_type = file.excel_file.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in EXCEL_FILE_TYPES:
            context = {
                'all_projects': projects,
                'all_files': File.objects.all(),
                'project': project,
                'form': form,
                'error_message': 'File must be XLS, XLSX',
            }
            return render(request, 'rfs/file_add.html', context)

        file.save()
        return render(request, 'rfs/file_add.html', {'project': project,'all_projects':projects,'form': form,})
    context = {
        'all_projects': projects,
        'all_files': File.objects.all(),
        'project': project,
        'form': form,
    }
    return render(request, 'rfs/file_add.html', context)

"""
class FileAdd(TemplateView):
    model=File
    template_name='rfs/file_add.html'
    fields=['file_name']

    def get_context_data(self,**kwargs):
        context=super(FileAdd,self).get_context_data(**kwargs)
        context['all_projects']=Project.objects.all()
        context['all_files'] = File.objects.all()
        return context
"""