from django.views import generic
from django.views.generic import View,TemplateView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.core.urlresolvers import reverse_lazy,reverse
from .forms import UserForm,FileForm
from .models import Project,File
from django.http import HttpResponse,Http404,HttpResponseRedirect



EXCEL_FILE_TYPES=['xlsx','xls']



def start_view(request):
    return redirect('rfs:login')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'rfs/base.html', {'all_projects': Project.objects.all(),
                                                         'user':request.user.username,})
            else:
                return render(request, 'rfs/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'rfs/login.html', {'error_message': 'Invalid login'})
    return render(request, 'rfs/login.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'rfs/login.html', context)


def index_view(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('rfs:login'))
    else:
        context={'all_projects':Project.objects.all()}
        template_name='rfs/base.html'
        return render(request,template_name,context)

##########################PROJECT VIEWS
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

def file_view(request, project_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('rfs:login'))
    else:
        form = FileForm(request.POST or None, request.FILES or None)
        project=get_object_or_404(Project,pk=project_id)
        projects = Project.objects.all()
        if form.is_valid():
            project_files = project.file_set.all()
            for f in project_files:
                if f.excel_file == form.cleaned_data.get("excel_file"):
                    context = {
                        'all_projects': projects,
                        'all_files': File.objects.all(),
                        'project': project,
                        'form': form,
                        'error_message': 'You already added that file',
                    }
                    return render(request, 'rfs/file.html', context)
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
                return render(request, 'rfs/file.html', context)

            file.save()
            return render(request, 'rfs/file.html',
                          {'project': project,
                           'all_projects': projects,
                           'form': form,
                           })
        context = {
            'all_projects': projects,
            'all_files': File.objects.all(),
            'project': project,
            'form': form,
        }
        return render(request, 'rfs/file.html', context)

def file_delete(request, project_id, file_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('rfs:login'))
    else:
        file=File.objects.get(pk=file_id)
        file.delete()
        return HttpResponseRedirect(reverse('rfs:file', args=[project_id]))

def file_delete_in_details(request, project_id, file_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('rfs:login'))
    else:
        file = File.objects.get(pk=file_id)
        file.delete()
        return HttpResponseRedirect(reverse('rfs:project', args=[project_id]))

###########EXCELREADER#############
import os
from .excelReader import excel_reader
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read_excel(request):

    choice=request.POST.get('chosenFile')
    if choice==None:
        return render(request,'rfs/read_insert.html',{'files':File.objects.all(),})
    excelReader=excel_reader(str(BASE_DIR)+'/projects/'+str(choice))
    return render(request,'rfs/read_insert.html',{'output':(str(BASE_DIR)+'/projects/project_d/sample.xlsx'),
                                                  'files':File.objects.all(),
                                                  'return':excelReader,
                                                  'choice':choice
                                                  })

