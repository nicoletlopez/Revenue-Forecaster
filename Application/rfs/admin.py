from django.contrib import admin
from .models import Project,File, Segment_list, Individual_segment, Group_segment, Actual, Forecast

admin.site.register(Project)
admin.site.register(File)
admin.site.register(Segment_list)
admin.site.register(Individual_segment)
admin.site.register(Group_segment)
admin.site.register(Actual)
admin.site.register(Forecast)
