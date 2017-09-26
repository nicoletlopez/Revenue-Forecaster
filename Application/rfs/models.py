from django.db import models
from django.core.urlresolvers import reverse

class Project(models.Model):
    project_name=models.CharField(max_length=50,unique=True)
    description=models.TextField(blank=True)
    #last_modified=models.DateTimeField(auto_now=True)
    #created_at=models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse('rfs:project',kwargs={'pk':self.pk})
    def __str__(self):
        return self.project_name
        #+'-'+self.last_modified+'-'+self.created_at

class File(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    excel_file=models.FileField()

class Segment_list(models.Model):
    SEG_TYPES= (
        ('IND','Individual'),
        ('GRP','Group'),
    )
    seg_id = models.CharField(max_length=15,primary_key=True)
    seg_type = models.CharField(max_length=10,choices=SEG_TYPES)
    def __str__(self):
        return str(self.seg_id) + " - %s" % self.seg_type
    class Meta:
        ordering = ['seg_type']

class Individual_segment(models.Model):
    ind_seg_id = models.OneToOneField(Segment_list,on_delete=models.CASCADE,primary_key=True)
    ind_seg_nme = models.CharField(max_length=25, )
    def __str__(self):
        return self.ind_seg_nme
    class Meta:
        ordering = ['ind_seg_id']

class Group_segment(models.Model):
    grp_seg_id = models.OneToOneField(Segment_list,on_delete=models.CASCADE,primary_key=True)
    grp_seg_nme = models.CharField(max_length=25)
    def __str__(self):
        return self.grp_seg_nme
    class Meta:
        ordering = ['grp_seg_id']

class Actual(models.Model):
    actual_id = models.AutoField(primary_key=True,)
    seg_id = models.ForeignKey(Segment_list, on_delete=models.CASCADE)
    date = models.DateField()
    budget_rns = models.FloatField()
    budget_arr = models.FloatField()
    budget_rev = models.FloatField()
    actual_rns = models.FloatField()
    actual_arr = models.FloatField()
    actual_rev = models.FloatField()
    def __str__(self):
        return str(self.actual_id) + " %s %s " % (self.seg_id,self.date)
    class Meta:
        ordering = ['actual_id']

class Forecast(models.Model):
    forecast_id = models.AutoField(primary_key=True)
    date = models.DateField()
    forecast_rns = models.FloatField()
    forecast_arr = models.FloatField()
    forecast_rev = models.FloatField()
    actual_reference = models.ManyToManyField(Actual)

"""
class SEGMENTATION_LIST(models.Model):
    SEG_ID=models.CharField(max_length=25,primary_key=True)
    SEG_TYPE=models.CharField(max_length=25)

class INDIVIDUAL_SEGMENT_MASTER(models.Model):
    IND_SEG_ID = models.OneToOneField(SEGMENTATION_LIST,primary_key=True,on_delete=models.CASCADE)
    IND_SEG_NAME=models.CharField(max_length=45)

class GROUP_SEGMENT_MASTER(models.Model):
    GRP_SEG_ID= models.OneToOneField(SEGMENTATION_LIST,primary_key=True,on_delete=models.CASCADE)
    GRP_SEG_NAME = models.CharField(max_length=45)

class ROOM_ACTUAL(models.Model):
    ACTUAL_ID=models.CharField(max_length=20,primary_key=True,unique=False)
    SEG_ID = models.OneToOneField(SEGMENTATION_LIST,primary_key=True,unique=False)
    PROJECT_ID = models.ForeignKey(Project)
    DATE = models.DateField()
    BUDGET_RNS = models.FloatField()
    BUDGET_ARR = models.FloatField()
    BUDGET_REVENUE = models.FloatField()
    ACTUAL_RNS = models.FloatField()
    ACTUAL_ARR = models.FloatField()
    ACTUAL_REVENUE = models.FloatField()

class ROOM_FORECAST(models.Model):
    FORECAST_ID=models.CharField(max,length=20,primary_key=True,unique=False)
    ACTUAL_ID = models.OneToOneField(max_length=45)
    SEG_ID = models.CharField(max_length=45)
    PROJECT_ID = models.OneToOneField(max_length=45)
    DATE = models.CharField(max_length=45)
    FORECAST_RNS = models.CharField(max_length=45)
    FORECAST_ARR = models.CharField(max_length=45)
    FORECAST_REVENUE = models.CharField(max_length=45)
"""