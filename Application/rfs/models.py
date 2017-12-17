from django.db import models
from django.core.urlresolvers import reverse
from django.core.files.storage import Storage,FileSystemStorage

class Project(models.Model):
    project_name=models.CharField(max_length=50,unique=True)
    description=models.TextField(blank=True)
    status_types=(('ARC','Archived'),('ACT','Active'))
    status=models.CharField(max_length=3,choices=status_types,default='ACT')
    #last_modified=models.DateTimeField(auto_now=True)
    #created_at=models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse('rfs:project',kwargs={'pk':self.pk})
    def __str__(self):
        return self.project_name
    class Meta:
        ordering = ['-id']

class CustomStorage(FileSystemStorage):
    def get_valid_name(self,name):
        return name
def project_directory_path(instance,filename):
    return 'project_{0}/{1}'.format(instance.project.project_name,filename)

class File(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    excel_file=models.FileField(upload_to=project_directory_path,storage=CustomStorage())
    status_types = (('ARC', 'Archived'), ('ACT', 'Active'))
    status = models.CharField(max_length=3, choices=status_types, default='ACT')

    def get_absolute_url(self):
        return reverse('rfs:file-delete',kwargs={'file_id':self.pk})
    def __str__(self):
        return str(self.excel_file)

class Seg_list(models.Model):
    SEG_TYPES = (
        ('IND', 'Individual'),
        ('GRP', 'Group'),
    )
    tag = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    seg_type = models.CharField(max_length=30,choices=SEG_TYPES)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['id']
        unique_together = ("tag","name")

class Ind_seg(models.Model):
    ind = models.OneToOneField(Seg_list,on_delete=models.CASCADE,
                                  primary_key=True)
    tag = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['ind_id']

class Grp_seg(models.Model):
    grp = models.OneToOneField(Seg_list,on_delete=models.CASCADE,
                                  primary_key=True)
    tag = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['grp_id']

class Actual(models.Model):
    actual_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    segment = models.ForeignKey(Seg_list, on_delete=models.CASCADE,blank=True)
    date = models.DateField()
    #budget_rns = models.FloatField()
    #budget_arr = models.FloatField()
    #budget_rev = models.FloatField()
    actual_rns = models.DecimalField(max_digits=15,decimal_places=2,null=True)
    actual_arr = models.DecimalField(max_digits=15,decimal_places=2,null=True)
    actual_rev = models.DecimalField(max_digits=15,decimal_places=2,null=True)
    #still manually entered
    actual_rna = models.DecimalField(max_digits=15,decimal_places=2,null=True)

    #derived by actual_rns/actual_rna
    actual_ocr = models.DecimalField(max_digits=15,decimal_places=2,null=True)
    actual_revpar = models.DecimalField(max_digits=15,decimal_places=2,null=True)

    @property
    def ocr_percent(self):
        if self.actual_ocr is not None:
            return str(int(self.actual_ocr * 100))+"%"

    def __str__(self):
        return str(self.actual_id) + " - %s %s " % (self.segment,self.date)
    class Meta:
        ordering = ['actual_id']
        unique_together=(('project','date','actual_rns','actual_arr','actual_rev'))

class Forecast(models.Model):
    forecast_id = models.AutoField(primary_key=True)
    date = models.DateField()
    forecast_rns = models.DecimalField(max_digits=15,decimal_places=2)
    forecast_arr = models.DecimalField(max_digits=15,decimal_places=2)
    forecast_rev = models.DecimalField(max_digits=15,decimal_places=2)
    actual_reference = models.ManyToManyField(Actual)
    def __str__(self):
        return str(self.forecast_id) + " - %s " % self.date
    unique_together = (('forecast_rns','forecast_arr','forecast_rev','actual_reference'))