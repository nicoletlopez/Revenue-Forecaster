#from __future__ import print_function
from django.views import generic
from django.views.generic import View,TemplateView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy,reverse
from .forms import UserForm,FileForm,CreateForm,XlToDbForm
from .models import Project,File, Actual, Forecast, Seg_list
from django.http import HttpResponse,Http404,HttpResponseRedirect
from os.path import join, dirname, abspath
import datetime, xlrd,numpy as np
from xlrd.sheet import ctype_text

EXCEL_FILE_TYPES=['xlsx','xls']

def start_view(request):
    if request.user.is_authenticated():
        logout(request)
        return render(request, 'rfs/login.html', {'error_message': 'Logged out'})
    return redirect('rfs:login')

def login_view(request):
    if request.user.is_authenticated():
        logout(request)
        return render(request,'rfs/login.html',{'error_message':'Logged out'})
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'rfs/base.html', {'all_projects': Project.objects.all().filter(status='ACT'),
                                                             'user':request.user.username,})
                else:
                    return render(request, 'rfs/login.html', {'error_message': 'Your account has been disabled'})
            else:
                return render(request, 'rfs/login.html', {'error_message': 'Invalid login'})
        return render(request, 'rfs/login.html')

def logout_user(request):
    logout(request)
    #form = UserForm(request.POST or None)
    context = {
        "error_message":'Logged out'
    }
    return render(request,'rfs/login.html',context)


def index_view(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('rfs:login'))
    else:
        context={'all_projects':Project.objects.all().filter(status='ACT'),
                 'arc_projects':Project.objects.all().filter(status='ARC'),}
        template_name='rfs/base.html'
        return render(request,template_name,context)

##########################PROJECT VIEWS#######################
class ProjectDetail(LoginRequiredMixin,DetailView):
    login_url = 'rfs:login'
    redirect_field_name = ''
    model=Project
    template_name='rfs/project.html'

    def get_context_data(self,**kwargs):
        context=super(ProjectDetail,self).get_context_data(**kwargs)
        context['all_projects']=Project.objects.all().filter(status='ACT')
        context['all_files']=File.objects.all()
        context['arc_projects']=Project.objects.all().filter(status='ARC')
        return context

class ProjectCreate(LoginRequiredMixin,CreateView):
    login_url='rfs:login'
    redirect_field_name='redirect_to'
    model=Project
    template_name='rfs/project_create.html'
    form_class = CreateForm
    def get_context_data(self,**kwargs):
        context=super(ProjectCreate,self).get_context_data(**kwargs)
        context['all_projects']=Project.objects.all().filter(status='ACT')
        context['arc_projects'] = Project.objects.all().filter(status='ARC')
        return context

class ProjectUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'rfs:login'
    redirect_field_name = 'redirect_to'
    model=Project
    fields=['status']
    #success_url=reverse_lazy('rfs:project',kwargs={'pk':kwargs['asas']})


def file_view(request, project_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('rfs:login'))
    else:
        form = FileForm(request.POST or None, request.FILES or None)
        project=get_object_or_404(Project,pk=project_id)
        projects = Project.objects.all().filter(status='ACT')
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
                        'arc_projects': Project.objects.all().filter(status='ARC'),
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
                    'arc_projects': Project.objects.all().filter(status='ARC'),
                }
                return render(request, 'rfs/file.html', context)

            file.save()
            return render(request, 'rfs/file.html',
                          {'project': project,
                           'all_projects': projects,
                           'form': form,
                           'arc_projects': Project.objects.all().filter(status='ARC'),
                           })
        context = {
            'all_projects': projects,
            'all_files': File.objects.all(),
            'project': project,
            'form': form,
            'arc_projects': Project.objects.all().filter(status='ARC'),
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
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def excel_to_db(request):
    ##django##
    form = XlToDbForm(request.POST or None)
    if form.is_valid():
        excelfile=BASE_DIR+'/projects/'+str(form.cleaned_data.get("file"))
    ##enddjango##
        xl_workbook = xlrd.open_workbook(excelfile)
        #xl_workbook = xlrd.open_workbook('2015 ROOMS SEGMENTATION.xlsx')  # location and name of the file
        xl_sheet = xl_workbook.sheet_by_index(4)
        #print('Sheet name: %s' % xl_sheet.name)
        row = xl_sheet.row(4)
        ind_or_grp = xl_sheet.row(3)
        for iog, cell_obj in enumerate(ind_or_grp):
            if cell_obj.value == 'GROUP':
                group_start = iog
                #print('%s' % group_start)
        ind_actual = np.zeros((13, 12),
                              dtype=[('subsegment', 'S40'), ('month', 'S40'), ('rns', float), ('arr', float),
                                     ('rev', float)])
        grp_actual = np.zeros((5, 12), dtype=[('rns', 'f8'), ('arr', 'f8'), ('rev', 'f8')])

        month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                      'November', 'December']
        #print('(Column #) type:value')
        unneeded_columns = ['', 'Barter', 'GRAND TOTAL', 'TOTAL GROUP', 'TOTAL INDIVIDUAL', 'SEGMENT NAME',
                            'Qualified Discount', 'Long Staying']
        year=form.cleaned_data.get("year")
        #year = 2015 #"""URGENT: YEAR MUST BE CHANGEABLE"""
        def getDate(month, year):
            thirty_ones = ["January", "March", "May", "July", "August", "October", "December"]
            # thirties = ["February","April","June","September","November"]
            monthMap = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8,
                        "September": 9, "October": 10, "November": 11,
                        "December": 12}
            if month in thirty_ones:
                day = 31
            else:
                day = 30
            month = monthMap.get(month)
            date = "%s-%s-%s" % (year, month, day)
            return date

        ss = 0
        m = 0
        erow = 7
        for idx, cell_obj in enumerate(row):
            # only gets the subsegment
            subsegment = cell_obj.value  # use .value to get the value (duh)
            if subsegment not in unneeded_columns:  # get the Subsegment (rack, group, etc)
                # print('(%s) %s' % (idx, subsegment))
                mon = 5
                monx = 0
                for month in month_list:  # get the month (January, February etc)
                    # print(month)
                    ind_actual[ss, m]['subsegment'] = subsegment
                    ind_actual[ss, m]['month'] = month
                    mon = mon + monx
                    for x in range(0,
                                   3):  # get the column headers (Room Nights Sold, Average Rm Rate(PHP), Revenue (PHP'000)
                        ecolumn = idx + x
                        if x == 0:
                            val = 'rns'
                        elif x == 1:
                            val = 'arr'
                        else:
                            val = 'rev'
                        our = xl_sheet.cell(erow, ecolumn).value
                        if isinstance(our, str):
                            our = 0.0
                        # print(type(our))
                        ind_actual[ss, m][val] = our
                        # print(m)
                        # print(erow)
                    erow += 4
                    m += 1
                ss += 1
                erow = 7
                m = 0

        for main in ind_actual:
            for sub in main:
                segment = sub[0].upper().decode('utf-8').strip()
                month = sub[1].decode('utf-8')
                rns = sub[2]
                arr = sub[3]
                rev = sub[4]
                date = getDate(month, year)
                try:
                    seg_id = Seg_list.objects.filter(name=segment).values('name') #get the seg_id from the seg list as a foreign key in the actual_row's subsegments
                    actual_row = Actual(date=getDate(month,year),actual_rns=rns,actual_arr=arr,actual_rev=rev,seg_id=seg_id)
                    actual_row.save()
                    #print("%s %s %s %s %s %s" % (date, segment, month, rns, arr, rev))
                    #seg_id_get_query = "select id from seg_list where name like  '%%%s' limit 1" % segment
                    #cur.execute(seg_id_get_query)
                    #seg_id = cur.fetchone()[0]
                    #insert_query = "insert into actual (date,rns,arr,rev,seg_id) values('%s',%s,%s,%s,%s)" % (
                    #    date, rns, arr, rev, seg_id)
                    #cur.execute(insert_query)
                    #conn.commit()
                except(Exception):
                    #print(Exception.__traceback__)
                    pass
            #print()
        #conn.close()
        context={'form':form,
                 'file':excelfile,
                 'year':year,
                 'message':'program worked but did it insert? >:3'}
        return render(request,'rfs/read_insert.html',context)

    return render(request,'rfs/read_insert.html',{'form':form})