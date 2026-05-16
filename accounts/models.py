from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    
    sr_no = models.IntegerField(default=0)

    admission_year = models.CharField(max_length=20)

    roll_no = models.CharField(max_length=20)

    prn_no = models.CharField(max_length=30)

    mobile_number = models.CharField(max_length=15)

    aadhar_number = models.CharField(max_length=20)
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    gender = models.CharField(max_length=10, choices=gender_choices)
    
    batch = models.CharField(max_length=20)
    course = models.CharField(max_length=50)
    year = models.CharField(max_length=20)

    father_name = models.CharField(max_length=100, blank=True)
    mother_name = models.CharField(max_length=100, blank=True)

    address = models.TextField(blank=True)

    fees_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name
