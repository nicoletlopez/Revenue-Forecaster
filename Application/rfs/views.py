# from __future__ import print_function


import os
import traceback
from datetime import datetime

from dateutil.relativedelta import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.core.urlresolvers import reverse
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
# custom libraries
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import FileForm, CreateForm, ForecastOptionsForm, CustomForecastForm, UpdateRnaForm
from .libraries.holtwinters import HoltWinters as hwinters
from .libraries.xlread import ExcelReader as xlread
from .libraries.xlwrite import ExcelWriter as xlwrite
from .models import Project, File, Actual, Seg_list

# end custom libraries

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXCEL_FILE_TYPES = ['xlsx', 'xls']

json_serializer = serializers.get_serializer("json")()


def start_view(request):
    if request.user.is_authenticated():
        return redirect('rfs:index')
    return redirect('rfs:login')


def login_view(request):
    if request.user.is_authenticated():
        logout(request)
        return render(request, 'rfs/login.html', {'error_message': 'Logged out'})
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('rfs:index')
                else:
                    return render(request, 'rfs/login.html', {'error_message': 'Your account has been disabled'})
            else:
                return render(request, 'rfs/login.html', {'error_message': 'Invalid login'})
        return render(request, 'rfs/login.html')


def logout_user(request):
    logout(request)
    # form = UserForm(request.POST or None)
    context = {
        "error_message": 'Logged out'
    }
    return render(request, 'rfs/login.html', context)


def index_view(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('rfs:login'))
    else:
        context = {'all_projects': Project.objects.all().filter(status='ACT'),
                   'arc_projects': Project.objects.all().filter(status='ARC'),
                   }
        template_name = 'rfs/home.html'
        return render(request, template_name, context)


def upload_file_to(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('rfs:login'))
    else:
        context = {'all_projects': Project.objects.all().filter(status='ACT'),
                   'arc_projects': Project.objects.all().filter(status='ARC'),
                   }
        return render(request, 'rfs/upload_file_to.html', context)


def project_update_index(request, project_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('rfs:login'))
    else:
        project = Project.objects.get(pk=project_id)
        project.status = str(request.POST.get("status"))
        project.save()
        return redirect('rfs:index')


##########################PROJECT VIEWS#######################


class ProjectDashboard(LoginRequiredMixin, DetailView):
    login_url = 'rfs:login'
    redirect_field_name = ''
    model = Project
    template_name = 'rfs/project_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectDashboard, self).get_context_data(**kwargs)
        context['all_projects'] = Project.objects.all().filter(status='ACT')
        context['all_files'] = File.objects.all()
        context['arc_projects'] = Project.objects.all().filter(status='ARC')
        context['act_files'] = File.objects.filter(status='ACT', project_id=self.kwargs['pk'])
        context['arc_files'] = File.objects.filter(status='ARC', project_id=self.kwargs['pk'])
        context['actual_data_list'] = Actual.objects.all().filter(project_id=self.kwargs['pk'])
        context['actual_revpar'] = Actual.objects.all().filter(project_id=self.kwargs['pk']).aggregate(
            Sum('actual_revpar'))
        context['actual_rev'] = Actual.objects.all().filter(project_id=self.kwargs['pk']).aggregate(Sum('actual_rev'))
        context['actual_rns'] = Actual.objects.all().filter(project_id=self.kwargs['pk']).aggregate(Sum('actual_rns'))
        context['actual_arr'] = Actual.objects.all().filter(project_id=self.kwargs['pk']).aggregate(Sum('actual_arr'))
        if Actual.objects.filter(project_id=self.kwargs['pk']):
            context['actual_ocr'] = round(
                (Actual.objects.all().filter(project_id=self.kwargs['pk']).aggregate(Sum('actual_ocr')))[
                    'actual_ocr__sum'] * 10, 2)

        return context


class GraphInd(LoginRequiredMixin, DetailView):
    login_url = 'rfs:login'
    redirect_field_name = ''
    model = Project
    template_name = 'rfs/project_dashboard.html'

    def get_context_data(self, **kwargs):
        segment = 'IND'
        context = super(GraphInd, self).get_context_data(**kwargs)
        context['all_projects'] = Project.objects.all().filter(status='ACT')
        context['all_files'] = File.objects.all()
        context['arc_projects'] = Project.objects.all().filter(status='ARC')
        context['act_files'] = File.objects.filter(status='ACT', project_id=self.kwargs['pk'])
        context['arc_files'] = File.objects.filter(status='ARC', project_id=self.kwargs['pk'])
        context['actual_data_list'] = Actual.objects.all().filter(project_id=self.kwargs['pk'])
        context['actual_revpar'] = Actual.objects.all().filter(project_id=self.kwargs['pk'],
                                                               segment_id__seg_type=segment).aggregate(
            Sum('actual_revpar'))
        context['actual_rev'] = Actual.objects.all().filter(project_id=self.kwargs['pk'],
                                                            segment_id__seg_type=segment).aggregate(Sum('actual_rev'))
        context['actual_rns'] = Actual.objects.all().filter(project_id=self.kwargs['pk'],
                                                            segment_id__seg_type=segment).aggregate(Sum('actual_rns'))
        context['actual_arr'] = Actual.objects.all().filter(project_id=self.kwargs['pk'],
                                                            segment_id__seg_type=segment).aggregate(Sum('actual_arr'))
        context['actual_ocr'] = round((Actual.objects.all().filter(project_id=self.kwargs['pk'],
                                                                   segment_id__seg_type=segment).aggregate(
            Sum('actual_ocr')))['actual_ocr__sum'] * 10, 2)
        context['active_tag'] = 'active'
        context['block_display'] = 'display:block;'
        context['current_page'] = 'current-page'
        return context


class GraphGrp(LoginRequiredMixin, DetailView):
    login_url = 'rfs:login'
    redirect_field_name = ''
    model = Project
    template_name = 'rfs/project_dashboard.html'

    def get_context_data(self, **kwargs):
        segment = 'GRP'
        context = super(GraphGrp, self).get_context_data(**kwargs)
        context['all_projects'] = Project.objects.all().filter(status='ACT')
        context['all_files'] = File.objects.all()
        context['arc_projects'] = Project.objects.all().filter(status='ARC')
        context['act_files'] = File.objects.filter(status='ACT', project_id=self.kwargs['pk'])
        context['arc_files'] = File.objects.filter(status='ARC', project_id=self.kwargs['pk'])
        context['actual_data_list'] = Actual.objects.all().filter(project_id=self.kwargs['pk'])
        context['actual_revpar'] = Actual.objects.all().filter(project_id=self.kwargs['pk'],
                                                               segment_id__seg_type=segment).aggregate(
            Sum('actual_revpar'))
        context['actual_rev'] = Actual.objects.all().filter(project_id=self.kwargs['pk'],
                                                            segment_id__seg_type=segment).aggregate(Sum('actual_rev'))
        context['actual_rns'] = Actual.objects.all().filter(project_id=self.kwargs['pk'],
                                                            segment_id__seg_type=segment).aggregate(Sum('actual_rns'))
        context['actual_arr'] = Actual.objects.all().filter(project_id=self.kwargs['pk'],
                                                            segment_id__seg_type=segment).aggregate(Sum('actual_arr'))
        context['actual_ocr'] = round((Actual.objects.all().filter(project_id=self.kwargs['pk'],
                                                                   segment_id__seg_type=segment).aggregate(
            Sum('actual_ocr')))['actual_ocr__sum'] * 10, 2)
        context['active_tag'] = 'active'
        context['block_display'] = 'display:block;'
        context['current_page'] = 'current-page'
        return context


class ProjectDetails(LoginRequiredMixin, DetailView):
    login_url = 'rfs:login'
    redirect_field_name = ''
    model = Project
    template_name = 'rfs/project_details.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetails, self).get_context_data(**kwargs)
        context['all_projects'] = Project.objects.all().filter(status='ACT')
        context['all_files'] = File.objects.all()
        context['arc_projects'] = Project.objects.all().filter(status='ARC')
        context['act_files'] = File.objects.filter(status='ACT', project_id=self.kwargs['pk'])
        context['arc_files'] = File.objects.filter(status='ARC', project_id=self.kwargs['pk'])
        context['active_tag'] = 'active'
        context['block_display'] = 'display:block;'
        context['current_page'] = 'current-page'
        return context


class ProjectCreate(LoginRequiredMixin, CreateView):
    login_url = 'rfs:login'
    redirect_field_name = 'redirect_to'
    model = Project
    template_name = 'rfs/project_create.html'
    form_class = CreateForm

    def get_context_data(self, **kwargs):
        context = super(ProjectCreate, self).get_context_data(**kwargs)
        context['all_projects'] = Project.objects.all().filter(status='ACT')
        context['arc_projects'] = Project.objects.all().filter(status='ARC')
        return context


class ProjectUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'rfs:login'
    redirect_field_name = 'redirect_to'
    model = Project
    fields = ['status']
    # success_url=reverse_lazy('rfs:project',kwargs={'pk':kwargs['asas']})


##FILE VIEW###################

def file_view(request, project_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('rfs:login'))
    else:
        form = FileForm(request.POST or None, request.FILES or None)
        project = get_object_or_404(Project, pk=project_id)
        projects = Project.objects.all().filter(status='ACT')
        if form.is_valid():
            project_files = project.file_set.all()
            input_file = 'project_{0}/{1}'.format(project.project_name, form.cleaned_data.get("excel_file"))
            for f in project_files:
                if f.excel_file == input_file:
                    context = {
                        'all_projects': projects,
                        'act_files': File.objects.filter(status='ACT', project_id=project_id),
                        'project': project,
                        'form': form,
                        'error_message': 'You already added that file',
                        'arc_projects': Project.objects.all().filter(status='ARC'),
                        'arc_files': File.objects.filter(status='ARC', project_id=project_id),
                        'active_tag': 'active',
                        'block_display': 'display:block;',
                        'current_page': 'current-page',
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
                    'act_files': File.objects.filter(status='ACT', project_id=project_id),
                    'project': project,
                    'form': form,
                    'error_message': 'File must be XLS, XLSX',
                    'arc_projects': Project.objects.all().filter(status='ARC'),
                    'arc_files': File.objects.filter(status='ARC', project_id=project_id),
                    'active_tag': 'active',
                    'block_display': 'display:block;',
                    'current_page': 'current-page',
                }
                return render(request, 'rfs/file.html', context)

            file.save()
            return render(request, 'rfs/file.html',
                          {'project': project,
                           'all_projects': projects,
                           'act_files': File.objects.filter(status='ACT', project_id=project_id),
                           'form': form,
                           'arc_projects': Project.objects.all().filter(status='ARC'),
                           'arc_files': File.objects.filter(status='ARC', project_id=project_id),
                           'active_tag': 'active',
                           'block_display': 'display:block;',
                           'current_page': 'current-page',
                           })
        context = {
            'all_projects': projects,
            'arc_files': File.objects.filter(status='ARC', project_id=project_id),
            'act_files': File.objects.filter(status='ACT', project_id=project_id),
            'project': project,
            'form': form,
            'arc_projects': Project.objects.all().filter(status='ARC'),
            'active_tag': 'active',
            'block_display': 'display:block;',
            'current_page': 'current-page',
        }
        return render(request, 'rfs/file.html', context)


def arc_file_view(request, project_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('rfs:login'))
    else:
        project = get_object_or_404(Project, pk=project_id)
        context = {
            'all_projects': Project.objects.all().filter(status='ACT'),
            'project': project,
            'arc_files': File.objects.filter(status='ARC', project_id=project_id),
            'arc_projects': Project.objects.all().filter(status='ARC'),
            'act_files': File.objects.filter(status='ACT', project_id=project_id),
            'active_tag': 'active',
            'block_display': 'display:block;',
            'current_page': 'current-page',
        }
        return render(request, 'rfs/file_archived.html', context)


def arc_file_update(request, project_id, file_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('rfs:login'))
    else:
        file = File.objects.get(pk=file_id)
        file.status = str(request.POST.get("status"))
        file.save()
        return HttpResponseRedirect(reverse('rfs:arc-file', args=[project_id]))


def file_update(request, project_id, file_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('rfs:login'))
    else:
        file = File.objects.get(pk=file_id)
        file.status = str(request.POST.get("status"))
        file.save()
        return HttpResponseRedirect(reverse('rfs:file', args=[project_id]))


###########EXCELREADER#############
def excel_to_db(request, project_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('rfs:login'))
    else:
        form = FileForm(request.POST or None, request.FILES or None)
        project = get_object_or_404(Project, pk=project_id)
        projects = Project.objects.all().filter(status='ACT')
        if form.is_valid():
            project_files = project.file_set.all()
            input_file = 'project_{0}/{1}'.format(project.project_name, form.cleaned_data.get("excel_file"))
            for f in project_files:
                if f.excel_file == input_file:
                    context = {
                        'all_projects': projects,
                        'act_files': File.objects.filter(status='ACT', project_id=project_id),
                        'project': project,
                        'form': form,
                        'error_message': 'File already used',
                        'arc_projects': Project.objects.all().filter(status='ARC'),
                        'arc_files': File.objects.filter(status='ARC', project_id=project_id),
                        'active_tag': 'active',
                        'block_display': 'display:block;',
                        'current_page': 'current-page',
                        'actual_data_list': Actual.objects.all().filter(project_id=project_id),
                    }
                    return render(request, 'rfs/datafeeder.html', context)
            file = form.save(commit=False)
            file.project = project
            file.excel_file = request.FILES['excel_file']
            file_type = file.excel_file.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in EXCEL_FILE_TYPES:
                context = {
                    'all_projects': projects,
                    'act_files': File.objects.filter(status='ACT', project_id=project_id),
                    'project': project,
                    'form': form,
                    'error_message': 'File must be XLS, XLSX',
                    'arc_projects': Project.objects.all().filter(status='ARC'),
                    'arc_files': File.objects.filter(status='ARC', project_id=project_id),
                    'active_tag': 'active',
                    'block_display': 'display:block;',
                    'current_page': 'current-page',
                    'actual_data_list': Actual.objects.all().filter(project_id=project_id),
                }
                return render(request, 'rfs/datafeeder.html', context)
            file.save()

            def record(result_array):
                for tuples in result_array:
                    print(tuples)
                    for single_array in tuples:
                        segment = (single_array[0].decode("utf-8")).upper().strip()
                        # print("%s %s" % (segment,type(segment)))
                        date = single_array[1].decode("utf-8")
                        rns = float(single_array[2])
                        arr = float(single_array[3])
                        rev = float(single_array[4])
                        segment_id = Seg_list.objects.get(name=segment)

                        actual_object = Actual(date=date, actual_rns=rns, actual_arr=arr, actual_rev=rev,
                                               segment=segment_id, project_id=project_id)
                        actual_object.save()

            try:
                excelfile = BASE_DIR + '/projects/' + str(input_file)

                excel_read = xlread.ExcelReader(excelfile)

                if excel_read.current_year == 2015:
                    record(excel_read.store_last_year_values_to_array())
                    record(excel_read.store_current_year_values_to_array())
                    print("Year is 2015")
                else:
                    record(excel_read.store_current_year_values_to_array())

                year = excel_read.current_year
                # print("%s %s %s %s %s" % (segment,date,rns,arr,rev))
            except:

                context = {'project': project,
                           'arc_projects': Project.objects.all().filter(status='ARC'),
                           'all_projects': Project.objects.all().filter(status='ACT'),
                           'act_files': File.objects.filter(status='ACT', project_id=project_id),
                           'form': form,
                           'actual_data_list': Actual.objects.all().filter(project_id=project_id),
                           'arc_files': File.objects.filter(status='ARC', project_id=project_id),
                           'error_message': 'Excel format wrong. Please choose a correct one'
                           }
                return render(request, 'rfs/datafeeder.html', context)

            context = {'project': project,
                       'message': 'Data insert success!',
                       'arc_projects': Project.objects.all().filter(status='ARC'),
                       'all_projects': Project.objects.all().filter(status='ACT'),
                       'act_files': File.objects.filter(status='ACT', project_id=project_id),
                       'year_detect': year,
                       'form': form,
                       'actual_data_list': Actual.objects.all().filter(project_id=project_id),
                       'arc_files': File.objects.filter(status='ARC', project_id=project_id),
                       'active_tag': 'active',
                       'block_display': 'display:block;',
                       'current_page': 'current-page',
                       }
            return render(request, 'rfs/datafeeder.html', context)
        context = {'project': project,
                   'arc_projects': Project.objects.all().filter(status='ARC'),
                   'all_projects': Project.objects.all().filter(status='ACT'),
                   'act_files': File.objects.filter(status='ACT', project_id=project_id),
                   'actual_data_list': Actual.objects.all().filter(project_id=project_id),
                   'form': form,
                   'arc_files': File.objects.filter(status='ARC', project_id=project_id),
                   'active_tag': 'active',
                   'block_display': 'display:block;',
                   'current_page': 'current-page',
                   }
        return render(request, 'rfs/datafeeder.html', context)


###########TRIPLE SMOOTHING#############
def forecast_form_default(request, project_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('rfs:login'))
    else:
        form = ForecastOptionsForm(request.POST or None)
        project = get_object_or_404(Project, pk=project_id)

        def add_one_month(date_input):
            # january
            thirties = [2, 4, 6, 9, 11]
            thirty_ones = [3, 5, 7, 8, 10, 12]
            if date_input.month == 1:
                try:
                    date_input += relativedelta(months=1)
                    date_input = date_input.replace(day=28)
                except:
                    return date_input
                finally:
                    return date_input

            if date_input.month in thirties:
                date_input += relativedelta(months=1)
                date_input = date_input.replace(day=31)
                return date_input

            if date_input.month in thirty_ones:
                date_input += relativedelta(months=1)
                try:
                    date_input = date_input.replace(day=31)
                except:
                    date_input = date_input.replace(day=30)
                finally:
                    return date_input

    if form.is_valid():
        # get forecast info
        # get performance metric desired
        metric = request.POST.get("metric")
        # get start date
        start_date = datetime.strptime(request.POST.get("start_date"), '%Y-%m-%d')
        # get end date
        end_date = datetime.strptime(request.POST.get("end_date"), '%Y-%m-%d')
        # get number of predictions
        n_preds = request.POST.get("number_of_predictions")
        # get fitting method
        fitting_method = request.POST.get("fitting_method")
        # get season length
        season_length = int(request.POST.get('season_length'))
        # get the segment (group or individual)
        segment = request.POST.get('segment')
        # get the constant values
        # alpha = request.POST.get("alpha")
        # beta = request.POST.get("beta")
        # gamma = request.POST.get("gamma")

        # get the starting,end, and skip constant values
        constant_value_start = request.POST.get("constant_value_start")

        # create an array for the values (e.g. total + group for month of january)
        value_list = []

        # add the total + group for each month
        # to keep track, increment a month for each query, and add each query to the value_count list
        date = start_date
        while date <= end_date:
            # for total
            if segment == 'TOTAL':
                total_value = Actual.objects.filter(date=date).aggregate(Sum('actual_%s' % metric))
            # for group or individual
            elif segment == 'IND' or segment == 'GRP':
                # segs = Seg_list.objects.filter(seg_type=segment)
                total_value = Actual.objects.filter(date=date, segment__seg_type=segment).aggregate(
                    Sum('actual_%s' % metric))
                # total_value = Actual.objects.filter(date=date, segment_id=segs).aggregate(Sum('actual_%s' % metric))
                # total_value = Actual.objects.filter(date=date, segment_id=segs)
            # for individual segments
            else:
                # segment_id = Seg_list.objects.get(tag=segment)
                total_value = Actual.objects.filter(date=date, segment__tag=segment).aggregate(
                    Sum('actual_%s' % metric))
            try:
                value_list.append(float(total_value['actual_%s__sum' % metric]))
            except:
                value_list.append(0)
            date = add_one_month(date)

        # make the necessary forecast using the HoltWinters class and the values in the value_count variable
        # if the data is less than the season length, an error will occur

        try:
            hw = hwinters.HoltWinters(value_list, int(n_preds), int(season_length))
            #
            prediction_tuples = hw.get_prediction_tuples(step=2)
            if fitting_method == 'sse':
                result = hw.optimize_by_sse(prediction_tuples)
            elif fitting_method == 'mad':
                result = hw.optimize_by_mad(prediction_tuples)
            elif fitting_method == 'mse':
                result = hw.optimize_by_mse(prediction_tuples)
        except Exception:
            result = "Data too short for season length %s" % season_length

        ###record results in excel file
        def write_to_excel(metric, subsegment, value, project_name='Project', month="DEFAULT", year='DEFAULT'):
            month_map = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July",
                         8: "August",
                         9: "September", 10: "October", 11: "November", 12: "December"}
            ind_map = {"RCK": "Rack", "CORP": "Corporate", "CORPO": "Corporate Others", "PKG/PRM": "Packages/Promo"
                , "WSOL": "Wholesale Online", "WSOF": "Wholesale Offline", "INDO": "Individual Others",
                       "INDR": "Industry Rate"}
            grp_map = {"CORPM": "Corporate Meetings", "CON/ASSOC": "Convention/Association", "GOV'T/NGOS": "Gov't/NGOs"
                , "GRPT": "Group Tours", "GRPO": "Group Others"}
            metric_dic = {"rev": "Revenue (000's)", "arr": "Avarage Room Rate"
                , "ocr": "Occupancy (%)", "revpar": "Revenue (000's)"}

            value = value[0]

            year = str(year)
            # month_string = month_map[month]
            writer = xlwrite.ExcelWriter(project_name, month, year)
            metric = metric_dic[metric]

            if subsegment in ind_map:
                segment = ind_map[subsegment]
                writer.insert_individual_forecast_value(value, segment, metric)
            elif subsegment in grp_map:
                segment = grp_map[subsegment]
                writer.insert_group_forecast_value(value, segment, metric)
            writer.save_file()

        project_name = Project.objects.get(id=project_id).project_name
        write_to_excel(metric, segment, result, project_name)

        return render(request, 'rfs/default_forecast_form.html', {
            'project': project,
            'form': form,
            'metric': metric,
            'start_date': start_date,
            'end_date': end_date,
            'segment': segment,
            'values_list': value_list,
            'n_preds': n_preds,
            'fitting_method': fitting_method,
            'season_length': season_length,
            'alpha': hw.constants[0],
            'beta': hw.constants[1],
            'gamma': hw.constants[2],
            'result': result,
            'arc_projects': Project.objects.all().filter(status='ARC'),
            'all_projects': Project.objects.all().filter(status='ACT'),
            'act_files': File.objects.filter(status='ACT', project_id=project_id),
            'actual_data_list': Actual.objects.all().filter(project_id=project_id),
            'arc_files': File.objects.filter(status='ARC', project_id=project_id),
            'active_tag': 'active',
            'block_display': 'display:block;',
            'current_page': 'current-page',
        })
    return render(request, 'rfs/default_forecast_form.html', {
        'project': project,
        'form': form,
        'arc_projects': Project.objects.all().filter(status='ARC'),
        'all_projects': Project.objects.all().filter(status='ACT'),
        'act_files': File.objects.filter(status='ACT', project_id=project_id),
        'actual_data_list': Actual.objects.all().filter(project_id=project_id),
        'arc_files': File.objects.filter(status='ARC', project_id=project_id),
        'active_tag': 'active',
        'block_display': 'display:block;',
        'current_page': 'current-page',
    })


def forecast_form_custom(request, project_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('rfs:login'))
    else:
        form = CustomForecastForm(request.POST or None)
        project = get_object_or_404(Project, pk=project_id)

        def add_one_month(date_input):
            thirties = [2, 4, 6, 9, 11]
            thirty_ones = [3, 5, 7, 8, 10, 12]

            if date_input.month == 1:
                try:
                    date_input += relativedelta(months=1)
                    date_input = date_input.replace(day=28)
                except:
                    return date_input
                finally:
                    return date_input

            if date_input.month in thirties:
                date_input += relativedelta(months=1)
                date_input = date_input.replace(day=31)
                return date_input

            if date_input.month in thirty_ones:
                date_input += relativedelta(months=1)
                try:
                    date_input = date_input.replace(day=31)
                except:
                    date_input = date_input.replace(day=30)
                finally:
                    return date_input

    if form.is_valid():
        metric = request.POST.get("metric")
        start_date = datetime.strptime(request.POST.get("start_date"), '%Y-%m-%d')
        end_date = datetime.strptime(request.POST.get("end_date"), '%Y-%m-%d')
        n_preds = request.POST.get("number_of_predictions")
        season_length = int(request.POST.get("season_length"))
        segment = request.POST.get("segment")

        alpha = float(request.POST.get('alpha'))
        beta = float(request.POST.get('beta'))
        gamma = float(request.POST.get('gamma'))

        constant_value_start = request.POST.get("constant_value_start")

        value_list = []

        date = start_date
        while (date <= end_date):
            if segment == 'TOTAL':
                total_value = Actual.objects.filter(date=date).aggregate(Sum('actual_%s' % metric))
            elif segment == 'IND' or segment == 'GRP':
                total_value = Actual.objects.filter(date=date, segment__seg_type=segment) \
                    .aggregate(Sum('actual_%s' % metric))
            else:
                total_value = Actual.objects.filter(date=date, segment__tag=segment).aggregate(
                    Sum('actual_%s' % metric))
            try:
                value_list.append(float(total_value['actual_%s__sum' % metric]))
            except:
                value_list.append(0)
            date = add_one_month(date)

        try:
            hw = hwinters.HoltWinters(value_list, int(n_preds), int(season_length))
            result = hw.triple_exponential_smoothing(alpha, beta, gamma)
            result = result[len(result) - 1]
        except Exception:
            traceback.print_exc()
            result = "Data too short for season length %s" % season_length

        return render(request, 'rfs/default_forecast_form.html',
                      {
                          'project': project,
                          'form': form,
                          'metric': metric,
                          'start_date': start_date,
                          'end_date': end_date,
                          'segment': segment,
                          'values_list': value_list,
                          'n_preds': n_preds,
                          'season_length': season_length,
                          'alpha': alpha,
                          'beta': beta,
                          'gamma': gamma,
                          'result': result,
                          'arc_projects': Project.objects.all().filter(status='ARC'),
                          'actual_data_list': Actual.objects.all().filter(project_id=project_id),
                          'arc_files': File.objects.filter(status='ARC', project_id=project_id),
                          'active_tag': 'active',
                          'block_display': 'display:block;',
                          'current_page': 'current-page',
                      })
    return render(request, 'rfs/default_forecast_form.html',
                  {
                      'project': project,
                      'form': form,
                      'arc_projects': Project.objects.all().filter(status='ARC'),
                      'all_projects': Project.objects.all().filter(status='ACT'),
                      'act_files': File.objects.filter(status='ACT', project_id=project_id),
                      'actual_data_list': Actual.objects.all().filter(project_id=project_id),
                      'arc_files': File.objects.filter(status='ARC', project_id=project_id),
                      'active_tag': 'active',
                      'block_display': 'display:block;',
                      'current_page': 'current-page',
                  })


"""def forecast_form_custom(request, project_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('rfs:login'))
    else:
        project = get_object_or_404(Project, pk=project_id)

        def add_one_month(date_input):
            # january
            thirties = [2, 4, 6, 9, 11]
            thirty_ones = [3, 5, 7, 8, 10, 12]
            if date_input.month == 1:
                try:
                    date_input += relativedelta(months=1)
                    date_input = date_input.replace(day=28)
                except:
                    return date_input
                finally:
                    return date_input

            if date_input.month in thirties:
                date_input += relativedelta(months=1)
                date_input = date_input.replace(day=31)
                return date_input

            if date_input.month in thirty_ones:
                date_input += relativedelta(months=1)
                try:
                    date_input = date_input.replace(day=31)
                except:
                    date_input = date_input.replace(day=30)
                finally:
                    return date_input

        form = CustomForecastForm(request.POST or None)
        if form.is_valid():
            # get forecast info
            # get performance metric desired
            metric = request.POST.get("metric")
            # get start date
            start_date = datetime.strptime(request.POST.get("start_date"), '%Y-%m-%d')
            # get end date
            end_date = datetime.strptime(request.POST.get("end_date"), '%Y-%m-%d')
            # get number of predictions
            n_preds = request.POST.get("number_of_predictions")
            # get fitting method
            # fitting_method = request.POST.get("fitting_method")
            # get season length
            season_length = int(request.POST.get('season_length'))

            # get the constant values
            alpha = request.POST.get("alpha")
            beta = request.POST.get("beta")
            gamma = request.POST.get("gamma")

            segment = request.POST.get("segment")
            # get the starting,end, and skip constant values
            constant_value_start = request.POST.get("constant_value_start")

            # create an array for the values (e.g. total + group for month of january)
            value_list = []

            # add the total + group for each month
            # to keep track, increment a month for each query, and add each query to the value_count list
            date = start_date

            while date <= end_date:
                # for total
                if segment == 'TOTAL':
                    total_value = Actual.objects.filter(date=date).aggregate(Sum('actual_%s' % metric))
                # for group or individual
                elif segment == 'IND' or segment == 'GRP':
                    # segs = Seg_list.objects.filter(seg_type=segment)
                    total_value = Actual.objects.filter(date=date, segment__seg_type=segment).aggregate(
                        Sum('actual_%s' % metric))
                    # total_value = Actual.objects.filter(date=date, segment_id=segs).aggregate(Sum('actual_%s' % metric))
                    # total_value = Actual.objects.filter(date=date, segment_id=segs)
                # for individual segments
                else:
                    # segment_id = Seg_list.objects.get(tag=segment)
                    total_value = Actual.objects.filter(date=date, segment__tag=segment).aggregate(
                        Sum('actual_%s' % metric))
                try:
                    value_list.append(float(total_value['actual_%s__sum' % metric]))
                except:
                    value_list.append(0)
                date = add_one_month(date)

            #while date <= end_date:
            #    total_value = Actual.objects.filter(date=date).aggregate(Sum('actual_%s' % metric))
            #    try:
            #        value_list.append(float(total_value['actual_%s__sum' % metric]))
            #    except:
            #        value_list.append(0)
            #    date = add_one_month(date)

            # make the necessary forecast using the HoltWinters class and the values in the value_count variable
            # if the data is less than the season length, an error will occur
            hw = hwinters.HoltWinters(value_list, int(n_preds), int(season_length))
            result = hw.triple_exponential_smoothing(float(alpha), float(beta), float(gamma))[-int(n_preds):]
            try:
                # hw = hwinters.HoltWinters(value_list, int(n_preds), int(season_length))
                # result = hw.triple_exponential_smoothing(alpha,beta,gamma)[-n_preds:]
                pass
            except Exception:
                pass
                # result = "Data too short for season length %s" % season_length

            return render(request, 'rfs/default_forecast_form.html', {'form': form,
                                                                      'project': project,
                                                                      "metric": metric,
                                                                      "start_date": start_date,
                                                                      "end_date": end_date,
                                                                      "values_list": value_list,
                                                                      "n_preds": n_preds,
                                                                      "season_length": season_length,
                                                                      "alpha": alpha,  # hw.constants[0][0],
                                                                      "beta": beta,  # hw.constants[1][0],
                                                                      "gamma": gamma,  # hw.constants[2][0],
                                                                      "result": result,
                                                                      'arc_projects': Project.objects.all().filter(
                                                                          status='ARC'),
                                                                      'all_projects': Project.objects.all().filter(
                                                                          status='ACT'),
                                                                      'act_files': File.objects.filter(status='ACT',
                                                                                                       project_id=project_id),
                                                                      'actual_data_list': Actual.objects.all().filter(
                                                                          project_id=project_id),
                                                                      'arc_files': File.objects.filter(status='ARC',
                                                                                                       project_id=project_id),
                                                                      'active_tag': 'active',
                                                                      'block_display': 'display:block;',
                                                                      'current_page': 'current-page',
                                                                      })

            # return render(request,'rfs/default_forecast_form.html',{"form":form,"values":values_dict})
        else:
            return render(request, 'rfs/default_forecast_form.html', {'form': form,
                                                                      'project': project,
                                                                      'arc_projects': Project.objects.all().filter(
                                                                          status='ARC'),
                                                                      'all_projects': Project.objects.all().filter(
                                                                          status='ACT'),
                                                                      'act_files': File.objects.filter(status='ACT',
                                                                                                       project_id=project_id),
                                                                      'actual_data_list': Actual.objects.all().filter(
                                                                          project_id=project_id),
                                                                      'arc_files': File.objects.filter(status='ARC',
                                                                                                       project_id=project_id),
                                                                      'active_tag': 'active',
                                                                      'block_display': 'display:block;',
                                                                      'current_page': 'current-page',
                                                                      })

    # a view for updating room nights sold in any given month
    """


def update_rns(request, project_id):
    form = UpdateRnaForm(request.POST or None)
    message = ''
    if form.is_valid():
        def check_valid_date(date):
            if Actual.objects.filter(date=date).exists():
                pass
            else:
                message = 'ERROR: Date does not exist'
                return render(request, 'rfs/update_rna_form.html', {"form": form, "message": message})

        segment = request.POST.get("segment")
        date = request.POST.get("date")
        rna = request.POST.get("rna")

        check_valid_date(date)

        actual_object = Actual.objects.filter(date=date).update(actual_rna=rna)
        # actual_object.save()

        message = "Set Room Nights Available to %s on date %s" % (rna, date)

    context = {"form": form, "message": message}

    return render(request, "rfs/update_rna_form.html", context=context)


class ChartData(APIView):

    def get(self, request, project_id, **kwargs):
        project = get_object_or_404(Project, pk=project_id)
        date_query = Actual.objects.filter(project=project).order_by('date').values_list('date', flat='true').distinct()
        date = []

        rev_total = []
        revpar_total = []
        arr_total = []
        rns_total = []
        ocr_total = []

        for x in range(len(date_query)):
            date.append(date_query[x].strftime('%B %Y'))

            actual_rev_query = Actual.objects.filter(project=project,
                                                     date=date_query[x].strftime('%Y-%m-%d')).aggregate(
                Sum('actual_rev'))
            # value = round(actual_rev_query['actual_rev__sum']/1000,2)
            rev_total.append(float(actual_rev_query['actual_rev__sum']))

            actual_arr_query = Actual.objects.filter(project=project,
                                                     date=date_query[x].strftime('%Y-%m-%d')).aggregate(
                Sum('actual_arr'))
            arr_total.append(float(actual_arr_query['actual_arr__sum']))

            actual_rns_query = Actual.objects.filter(project=project,
                                                     date=date_query[x].strftime('%Y-%m-%d')).aggregate(
                Sum('actual_rns'))
            rns_total.append(float(actual_rns_query['actual_rns__sum']))

            actual_revpar_query = Actual.objects.filter(project=project,
                                                        date=date_query[x].strftime('%Y-%m-%d')).aggregate(
                Sum('actual_revpar'))
            revpar_total.append(float(actual_revpar_query['actual_revpar__sum']))

            actual_ocr_query = Actual.objects.filter(project=project,
                                                     date=date_query[x].strftime('%Y-%m-%d')).aggregate(
                Sum('actual_ocr'))
            value = round(actual_ocr_query['actual_ocr__sum'] * 100)
            ocr_total.append(float(value))

        data = {
            # Mixed
            "rev_total": rev_total,
            "arr_total": arr_total,
            "rns_total": rns_total,
            "ocr_total": ocr_total,
            "revpar_total": revpar_total,

            "date": date,
        }
        return Response(data)


class ChartDataInd(APIView):

    def get(self, request, project_id, **kwargs):
        project = get_object_or_404(Project, pk=project_id)
        segment_ind = Seg_list.objects.filter(seg_type='IND').values_list('pk', flat='true')
        date_query = Actual.objects.filter(project=project).order_by('date').values_list('date', flat='true').distinct()
        date = []

        rev_total = []
        revpar_total = []
        arr_total = []
        rns_total = []
        ocr_total = []

        for x in range(len(date_query)):
            date.append(date_query[x].strftime('%B %Y'))

            # Individuals
            ind_actual_rev_total_query = Actual.objects.filter(project=project, date=date_query[x].strftime('%Y-%m-%d'),
                                                               segment__in=segment_ind).aggregate(Sum('actual_rev'))
            # value = round(ind_actual_rev_total_query['actual_rev__sum'] / 1000, 2)
            rev_total.append(float(ind_actual_rev_total_query['actual_rev__sum']))

            ind_actual_arr_total_query = Actual.objects.filter(project=project, date=date_query[x].strftime('%Y-%m-%d'),
                                                               segment__in=segment_ind).aggregate(Sum('actual_arr'))
            arr_total.append(float(ind_actual_arr_total_query['actual_arr__sum']))

            ind_actual_rns_total_query = Actual.objects.filter(project=project, date=date_query[x].strftime('%Y-%m-%d'),
                                                               segment__in=segment_ind).aggregate(Sum('actual_rns'))
            rns_total.append(float(ind_actual_rns_total_query['actual_rns__sum']))

            ind_actual_revpar_total_query = Actual.objects.filter(project=project,
                                                                  date=date_query[x].strftime('%Y-%m-%d'),
                                                                  segment__in=segment_ind).aggregate(
                Sum('actual_revpar'))
            revpar_total.append(float(ind_actual_revpar_total_query['actual_revpar__sum']))

            ind_actual_ocr_total_query = Actual.objects.filter(project=project, date=date_query[x].strftime('%Y-%m-%d'),
                                                               segment__in=segment_ind).aggregate(Sum('actual_ocr'))
            value = round(ind_actual_ocr_total_query['actual_ocr__sum'] * 100)
            ocr_total.append(float(value))

        data = {
            # Individual
            "rev_total": rev_total,
            "arr_total": arr_total,
            "rns_total": rns_total,
            "revpar_total": revpar_total,
            "ocr_total": ocr_total,

            "date": date,
        }
        return Response(data)


class ChartDataGrp(APIView):

    def get(self, request, project_id, **kwargs):
        project = get_object_or_404(Project, pk=project_id)
        segment_grp = Seg_list.objects.filter(seg_type='GRP').values_list('pk', flat='true')
        date_query = Actual.objects.filter(project=project).order_by('date').values_list('date', flat='true').distinct()
        date = []

        rev_total = []
        revpar_total = []
        arr_total = []
        rns_total = []
        ocr_total = []

        for x in range(len(date_query)):
            date.append(date_query[x].strftime('%B %Y'))

            # Group
            grp_actual_rev_total_query = Actual.objects.filter(project=project, date=date_query[x].strftime('%Y-%m-%d'),
                                                               segment__in=segment_grp).aggregate(Sum('actual_rev'))
            # value = round(grp_actual_rev_total_query['actual_rev__sum'] / 1000, 2)
            rev_total.append(float(grp_actual_rev_total_query['actual_rev__sum']))
            grp_actual_arr_total_query = Actual.objects.filter(project=project, date=date_query[x].strftime('%Y-%m-%d'),
                                                               segment__in=segment_grp).aggregate(Sum('actual_arr'))
            arr_total.append(float(grp_actual_arr_total_query['actual_arr__sum']))
            grp_actual_rns_total_query = Actual.objects.filter(project=project, date=date_query[x].strftime('%Y-%m-%d'),
                                                               segment__in=segment_grp).aggregate(Sum('actual_rns'))
            rns_total.append(float(grp_actual_rns_total_query['actual_rns__sum']))
            grp_actual_revpar_total_query = Actual.objects.filter(project=project,
                                                                  date=date_query[x].strftime('%Y-%m-%d'),
                                                                  segment__in=segment_grp).aggregate(
                Sum('actual_revpar'))
            revpar_total.append(float(grp_actual_revpar_total_query['actual_revpar__sum']))
            grp_actual_ocr_total_query = Actual.objects.filter(project=project, date=date_query[x].strftime('%Y-%m-%d'),
                                                               segment__in=segment_grp).aggregate(Sum('actual_ocr'))
            value = round(grp_actual_ocr_total_query['actual_ocr__sum'] * 100)
            ocr_total.append(float(value))

        data = {
            # Group
            "rev_total": rev_total,
            "arr_total": arr_total,
            "rns_total": rns_total,
            "ocr_total": ocr_total,
            "revpar_total": revpar_total,

            "date": date,
        }
        return Response(data)
