from django.db import models
import datetime

class Project(models.Model):
    projectname = models.CharField(verbose_name="Project Name", max_length=50)

    def __str__(self):
        return self.projectname

class Procurement(models.Model):
    reqnumber = models.CharField(verbose_name="REQ Number", max_length=15)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    reqcreated = models.DateField(verbose_name="REQ Created", default=None, blank=True, null=True)
    reqstatus = models.CharField(verbose_name="REQ Status", max_length=50)
    description = models.CharField(verbose_name="Description", max_length=50)
    prnumber = models.CharField(verbose_name="PR Number", max_length=20)
    ponumber = models.CharField(verbose_name="PO Number", max_length=20)
    postatus = models.CharField(verbose_name="PO Status", max_length=50)
    povendor = models.CharField(verbose_name="PO Vendor", max_length=50)
    pomaterial = models.CharField(verbose_name="PO Material",max_length=50)
    poprice = models.CharField(verbose_name="PO Price (USD)",max_length=20)
    pocreated = models.DateField(verbose_name="PO Created",default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.reqnumber} {self.description}'
