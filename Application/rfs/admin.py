from django.contrib import admin
from .models import Project,File, Seg_list, Ind_seg, Grp_seg, Actual, Forecast

class ProjectList(admin.ModelAdmin):
    list_display = ('project_name', 'description', 'status')

class FileList(admin.ModelAdmin):
    list_display = ('project', 'status')
    list_filter = ('project', 'status')

class Seg_listList(admin.ModelAdmin):
    list_display = ('name', 'seg_type')
    list_filter = ('seg_type', 'name')

class ActualList(admin.ModelAdmin):
    list_display = ('segment', 'project', 'date', 'actual_id')
    list_filter = ('segment', 'project')

class ForecastList(admin.ModelAdmin):
    list_display = ('forecast_id', 'date')


admin.site.register(Project, ProjectList)
admin.site.register(File, FileList)
admin.site.register(Seg_list, Seg_listList)
admin.site.register(Ind_seg)
admin.site.register(Grp_seg)
admin.site.register(Actual, ActualList)
admin.site.register(Forecast, ForecastList)

admin.site.site_header = 'Django Admin'
admin.site.index_title = 'Revenue Forecasting System'