from django.db import models


class Faculty(models.Model):

    sr_no = models.IntegerField()

    teacher_name = models.CharField(max_length=200)

    designation = models.CharField(max_length=100)

    dob = models.DateField()

    mobile_no = models.CharField(max_length=15)

    email_id = models.EmailField()

    osac_id = models.CharField(max_length=100)

    ug_experience = models.CharField(max_length=100)

    pg_experience = models.CharField(max_length=100)

    pg_passing_year = models.CharField(max_length=10)

    aadhar_no = models.CharField(max_length=20)

    pan_no = models.CharField(max_length=20)

    department = models.CharField(max_length=200)

    joining_date = models.DateField()

    def __str__(self):
        return self.teacher_name
