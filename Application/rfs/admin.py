from django.contrib import admin
from .models import Project,File, Seg_list, Ind_seg, Grp_seg, Actual, Forecast

admin.site.register(Project)
admin.site.register(File)
admin.site.register(Seg_list)
admin.site.register(Ind_seg)
admin.site.register(Grp_seg)
admin.site.register(Actual)
admin.site.register(Forecast)