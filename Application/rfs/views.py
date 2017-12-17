# from __future__ import print_function


import os
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

from .forms import FileForm, CreateForm, ForecastOptionsForm, CustomForecastForm, InputForm
from .libraries.holtwinters import HoltWinters as hwinters
from .libraries.xlread import ExcelReader as xlread
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
        return context

class GraphInd(LoginRequiredMixin,DetailView):
    login_url = 'rfs:login'
    redirect_field_name = ''
    model = Project
    template_name = 'rfs/project_dashboard.html'
    def get_context_data(self, **kwargs):
        context = super(GraphInd, self).get_context_data(**kwargs)
        context['all_projects'] = Project.objects.all().filter(status='ACT')
        context['all_files'] = File.objects.all()
        context['arc_projects'] = Project.objects.all().filter(status='ARC')
        context['act_files'] = File.objects.filter(status='ACT', project_id=self.kwargs['pk'])
        context['arc_files'] = File.objects.filter(status='ARC', project_id=self.kwargs['pk'])
        context['actual_data_list'] = Actual.objects.all().filter(project_id=self.kwargs['pk'])
        context['active_tag'] = 'active'
        context['block_display'] = 'display:block;'
        context['current_page'] = 'current-page'
        return context

class GraphGrp(LoginRequiredMixin,DetailView):
    login_url = 'rfs:login'
    redirect_field_name = ''
    model = Project
    template_name = 'rfs/project_dashboard.html'
    def get_context_data(self, **kwargs):
        context = super(GraphGrp, self).get_context_data(**kwargs)
        context['all_projects'] = Project.objects.all().filter(status='ACT')
        context['all_files'] = File.objects.all()
        context['arc_projects'] = Project.objects.all().filter(status='ARC')
        context['act_files'] = File.objects.filter(status='ACT', project_id=self.kwargs['pk'])
        context['arc_files'] = File.objects.filter(status='ARC', project_id=self.kwargs['pk'])
        context['actual_data_list'] = Actual.objects.all().filter(project_id=self.kwargs['pk'])
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
        context['active_tag']= 'active'
        context['block_display']= 'display:block;'
        context['current_page']= 'current-page'
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
            for f in project_files:
                if f.excel_file == form.cleaned_data.get("excel_file"):
                    context = {
                        'all_projects': projects,
                        'act_files': File.objects.filter(status='ACT', project_id=project_id),
                        'project': project,
                        'form': form,
                        'error_message': 'You already added that file',
                        'arc_projects': Project.objects.all().filter(status='ARC'),
                        'arc_files': File.objects.filter(status='ARC', project_id=project_id),
                        'active_tag':'active',
                        'block_display':'display:block;',
                        'current_page':'current-page',
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
    project = get_object_or_404(Project, pk=project_id)

    def record(result_array):
        for tuples in result_array:
            for single_array in tuples:
                segment = (single_array[0].decode("utf-8")).upper()
                date = single_array[1].decode("utf-8")
                rns = float(single_array[2])
                arr = float(single_array[3])
                rev = float(single_array[4])
                segment_id = Seg_list.objects.get(name=segment)
                actual_object = Actual(date=date, actual_rns=rns, actual_arr=arr, actual_rev=rev,
                                       segment=segment_id, project_id=project_id)
                actual_object.save()
    try:
        if request.method == "POST":

            excelfile = BASE_DIR + '/projects/' + str(request.POST.get("file"))
            # instantiate excel reader object
            excel_read = xlread.ExcelReader(excelfile)

            if excel_read.current_year == 2015:
                record(excel_read.store_last_year_values_to_array())
                record(excel_read.store_current_year_values_to_array())
            else:
                record(excel_read.store_current_year_values_to_array())

            year = excel_read.current_year


                #print("%s %s %s %s %s" % (segment,date,rns,arr,rev))



        context = {'project': project,
                   'arc_projects': Project.objects.all().filter(status='ARC'),
                   'all_projects': Project.objects.all().filter(status='ACT'),
                   'act_files': File.objects.filter(status='ACT', project_id=project_id),
                   'actual_data_list': Actual.objects.all().filter(project_id=project_id),
                   'arc_files': File.objects.filter(status='ARC', project_id=project_id),
                   'active_tag': 'active',
                   'block_display': 'display:block;',
                   'current_page': 'current-page',
                   }
        return render(request, 'rfs/datafeeder.html', context)
    except:
        context = {'project': project,
                   'message': 'Data insert success!',
                   'arc_projects': Project.objects.all().filter(status='ARC'),
                   'all_projects': Project.objects.all().filter(status='ACT'),
                   'act_files': File.objects.filter(status='ACT', project_id=project_id),
                   #'year_detect': year,
                   'actual_data_list': Actual.objects.all().filter(project_id=project_id),
                   'arc_files': File.objects.filter(status='ARC', project_id=project_id),
                   'active_tag': 'active',
                   'block_display': 'display:block;',
                   'current_page': 'current-page',
                   }
        return render(request, 'rfs/datafeeder.html', context)


"""
    context = {'project': project,
               'arc_projects': Project.objects.all().filter(status='ARC'),
               'all_projects': Project.objects.all().filter(status='ACT'),
               'act_files': File.objects.filter(status='ACT', project_id=project_id),
               'actual_data_list': Actual.objects.all().filter(project_id=project_id),
               'arc_files': File.objects.filter(status='ARC', project_id=project_id),
               'message': 'Excel format wrong. Please choose a correct one'
               }
    return render(request, 'rfs/datafeeder.html', context)
"""

###########TRIPLE SMOOTHING#############
def forecast_form_default(request, project_id):
    form = ForecastOptionsForm(request.POST or None)
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

        # get the constant values
        # alpha = request.POST.get("alpha")
        # beta = request.POST.get("beta")
        # gamma = request.POST.get("gamma")

        # get the starting,end, and skip constant values
        constant_value_start = request.POST.get("constant_value_start")

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

        # create an array for the values (e.g. total + group for month of january)
        value_list = []

        # add the total + group for each month
        # to keep track, increment a month for each query, and add each query to the value_count list
        date = start_date
        while date <= end_date:
            total_value = Actual.objects.filter(date=date).aggregate(Sum('actual_%s' % metric))
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
            prediction_tuples = hw.get_prediction_tuples(step=1)
            if fitting_method == 'sse':
                result = hw.optimize_by_sse(prediction_tuples)
            elif fitting_method == 'mad':
                result = hw.optimize_by_mad(prediction_tuples)
            elif fitting_method == 'mse':
                result = hw.optimize_by_mse(prediction_tuples)
        except Exception:
            result = "Data too short for season length %s" % season_length

        return render(request, 'rfs/default_forecast_form.html', {'form': form,
                                                                  "metric": metric,
                                                                  "start_date": start_date,
                                                                  "end_date": end_date,
                                                                  "values_list": value_list,
                                                                  "n_preds": n_preds,
                                                                  "fitting_method": fitting_method,
                                                                  "season_length": season_length,
                                                                  "alpha": hw.constants[0],
                                                                  "beta": hw.constants[1],
                                                                  "gamma": hw.constants[2],
                                                                  "result": result, },
                      )

        # return render(request,'rfs/default_forecast_form.html',{"form":form,"values":values_dict})

    return render(request, 'rfs/default_forecast_form.html', {'form': form})


def forecast_form_custom(request, project_id):
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

        # get the starting,end, and skip constant values
        constant_value_start = request.POST.get("constant_value_start")

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

        # create an array for the values (e.g. total + group for month of january)
        value_list = []

        # add the total + group for each month
        # to keep track, increment a month for each query, and add each query to the value_count list
        date = start_date
        while date <= end_date:
            total_value = Actual.objects.filter(date=date).aggregate(Sum('actual_%s' % metric))
            try:
                value_list.append(float(total_value['actual_%s__sum' % metric]))
            except:
                value_list.append(0)
            date = add_one_month(date)

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
                                                                  "metric": metric,
                                                                  "start_date": start_date,
                                                                  "end_date": end_date,
                                                                  "values_list": value_list,
                                                                  "n_preds": n_preds,
                                                                  "season_length": season_length,
                                                                  "alpha": "TEMP",  # hw.constants[0][0],
                                                                  "beta": "TEMP",  # hw.constants[1][0],
                                                                  "gamma": "TEMP",  # hw.constants[2][0],
                                                                  "result": result, }, )

        # return render(request,'rfs/default_forecast_form.html',{"form":form,"values":values_dict})
    else:
        return render(request, 'rfs/default_forecast_form.html', {'form': form})

def input_data(request,project_id):
    form = InputForm(request.POST or None)

    segment = request.POST.get("segment")
    date = request.POST.get("date")

    context = {"form":form}

    return render(request,"rfs/data_input_form.html",context=context)

class ChartData(APIView):

    def get(self, request, project_id,**kwargs):
        project=get_object_or_404(Project,pk=project_id)
        segment_ind = Seg_list.objects.filter(seg_type='IND').values_list('pk', flat='true')
        date_query = Actual.objects.filter(project=project).order_by('date').values_list('date', flat='true').distinct()
        date = []

        rev_total = []
        arr_total = []
        rns_total = []


        for x in range(len(date_query)):
            date.append(date_query[x].strftime('%B %Y'))

            actual_rev_query = Actual.objects.filter(project=project,date=date_query[x].strftime('%Y-%m-%d')).aggregate(Sum('actual_rev'))

            value = round(actual_rev_query['actual_rev__sum']/1000,2)
            rev_total.append(float(value))

            actual_arr_query = Actual.objects.filter(project=project,date=date_query[x].strftime('%Y-%m-%d')).aggregate(Sum('actual_arr'))
            arr_total.append(float(actual_arr_query['actual_arr__sum']))

            actual_rns_query = Actual.objects.filter(project=project,date=date_query[x].strftime('%Y-%m-%d')).aggregate(Sum('actual_rns'))
            rns_total.append(float(actual_rns_query['actual_rns__sum']))

        data = {
            #Mixed
            "rev_total": rev_total,
            "arr_total": arr_total,
            "rns_total": rns_total,
            "date": date,
        }
        return Response(data)
class ChartDataInd(APIView):

    def get(self, request, project_id,**kwargs):
        project=get_object_or_404(Project,pk=project_id)
        segment_ind = Seg_list.objects.filter(seg_type='IND').values_list('pk', flat='true')
        date_query = Actual.objects.filter(project=project).order_by('date').values_list('date', flat='true').distinct()
        date = []

        rev_total = []
        arr_total = []
        rns_total = []

        for x in range(len(date_query)):
            date.append(date_query[x].strftime('%B %Y'))
            segrev_total = 0
            segarr_total = 0
            segrns_total = 0

            # Individuals
            for individual_index in range(len(segment_ind)):
                ind_actual_rev_total_query = Actual.objects.filter(project=project, date=date_query[x].strftime('%Y-%m-%d'),segment=segment_ind[individual_index]).aggregate(Sum('actual_rev'))
                ind_rev_truncate = round(ind_actual_rev_total_query['actual_rev__sum']/1000,2)
                segrev_total += float(ind_rev_truncate)

                ind_actual_arr_total_query = Actual.objects.filter(project=project, date=date_query[x].strftime('%Y-%m-%d'),segment=segment_ind[individual_index]).aggregate(Sum('actual_arr'))
                segarr_total += float(ind_actual_arr_total_query['actual_arr__sum'])

                ind_actual_rns_total_query = Actual.objects.filter(project=project, date=date_query[x].strftime('%Y-%m-%d'),segment=segment_ind[individual_index]).aggregate(Sum('actual_rns'))
                segrns_total += float(ind_actual_rns_total_query['actual_rns__sum'])
        rev_total.append(segrev_total)
        arr_total.append(segarr_total)
        arr_total.append(segrns_total)

        data = {
            # Individual
            "rev_total": rev_total,
            "arr_total": arr_total,
            "rns_total": rns_total,
            "date": date,
        }
        return Response(data)
class ChartDataGrp(APIView):

    def get(self, request, project_id,**kwargs):
        project=get_object_or_404(Project,pk=project_id)
        segment_grp = Seg_list.objects.filter(seg_type='GRP').values_list('pk', flat='true')
        date_query = Actual.objects.filter(project=project).order_by('date').values_list('date', flat='true').distinct()
        date = []

        rev_total = []
        arr_total = []
        rns_total = []

        for x in range(len(date_query)):
            date.append(date_query[x].strftime('%B %Y'))

            # Group
            for group_index in range(len(segment_grp)):
                grp_actual_rev_total_query = Actual.objects.filter(project=project,date=date_query[x].strftime('%Y-%m-%d'),segment=segment_grp[segment_grp]).aggregate(Sum('actual_rev'))
                grp_rev_truncate = round(grp_actual_rev_total_query['actual_rev__sum'] / 1000, 2)
                rev_total.append(float(grp_rev_truncate))

                grp_actual_arr_total_query = Actual.objects.filter(project=project, date=date_query[x].strftime('%Y-%m-%d'), segment=segment_grp[group_index]).aggregate(Sum('actual_arr'))
                arr_total.append(float(grp_actual_arr_total_query['actual_arr__sum']))

                grp_actual_rns_total_query = Actual.objects.filter(project=project, date=date_query[x].strftime('%Y-%m-%d'),segment=segment_grp[group_index]).aggregate(Sum('actual_rns'))
                rns_total.append(float(grp_actual_rns_total_query['actual_rns__sum']))

        data = {
            # Individual
            "rev_total": rev_total,
            "arr_total": arr_total,
            "rns_total": rns_total,
            "date": date,
        }
        return Response(data)



