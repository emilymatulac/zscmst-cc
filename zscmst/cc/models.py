from django.db import models
from datetime import date

# # Create your models here.
# class Post(models.Model):
#     client_type = models.CharField(max_length=30)
#     # date = models.DateTimeField(auto_now_add = True)

#     def __str__(self):
#         return self.title

# class Evaluation(models.Model):
#     eval_id = models.AutoField(primary_key=True)
#     eval_citizenttype = models.CharField(max_length=30, default="")
#     eval_date = models.DateField(("Date"), default=date.today)
#     eval_sex = models.CharField(max_length=1, default="")
#     eval_age= models.IntegerField()
#     eval_region = models.CharField(max_length=30, default="")
#     eval_service = models.CharField(max_length=30, default="")
#     eval_cc1 = models.IntegerField(default=0)
#     eval_cc2 = models.IntegerField(default=0)
#     eval_cc3 = models.IntegerField(default=0)
#     eval_sqd0 = models.IntegerField(default=0)
#     eval_sqd1 = models.IntegerField(default=0)
#     eval_sqd2 = models.IntegerField(default=0)
#     eval_sqd3 = models.IntegerField(default=0)
#     eval_sqd4 = models.IntegerField(default=0)
#     eval_sqd5 = models.IntegerField(default=0)
#     eval_sqd6 = models.IntegerField(default=0)
#     eval_sqd7 = models.IntegerField(default=0)
#     eval_sqd8 = models.IntegerField(default=0)
#     eval_suggestion = models.CharField(max_length=250, default="")
#     eval_email = models.CharField(max_length=30, default="")

#     class Meta:
#         db_table = "tblcsqm"

class CitizenCharter(models.Model):
    eval_id = models.AutoField(primary_key=True)
    eval_citizenttype = models.CharField(max_length=50, default="")
    eval_date = models.CharField(max_length=50, default="")
    eval_sex = models.CharField(max_length=1, default="0")
    eval_age= models.IntegerField()
    eval_region = models.CharField(max_length=30, default="")
    eval_service = models.CharField(max_length=30, default="")
    eval_cc1 = models.IntegerField(default=0)
    eval_cc2 = models.IntegerField(default=0)
    eval_cc3 = models.IntegerField(default=0)
    eval_sqd0 = models.IntegerField(default=0)
    eval_sqd1 = models.IntegerField(default=0)
    eval_sqd2 = models.IntegerField(default=0)
    eval_sqd3 = models.IntegerField(default=0)
    eval_sqd4 = models.IntegerField(default=0)
    eval_sqd5 = models.IntegerField(default=0)
    eval_sqd6 = models.IntegerField(default=0)
    eval_sqd7 = models.IntegerField(default=0)
    eval_sqd8 = models.IntegerField(default=0)
    eval_suggestion = models.CharField(max_length=250, default="")
    eval_email = models.CharField(max_length=30, default="")
    eval_name = models.CharField(max_length=30, default="")
    eval_other = models.CharField(max_length=100, default="")
    office_id = models.IntegerField(default=0);

    class Meta:
        db_table = "tblcitizen"

class TableProcess(models.Model):
    process_id = models.AutoField(primary_key=True)
    office_id = models.IntegerField(default=0)
    process_desc = models.CharField(max_length=255)
    
    class Meta:
        db_table = "tblprocess"

class TableOffice(models.Model):
    office_id = models.AutoField(primary_key=True)
    office_code = models.CharField(max_length=20, default="0")
    office_desc = models.CharField(max_length=100)
    
    class Meta:
        db_table = "tbloffice"
