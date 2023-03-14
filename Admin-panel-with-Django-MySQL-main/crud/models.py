from django.db import models

# Create your models here.

class schedular(models.Model):

    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    CLASS_TYPE_CHOICES = (
        ('Lecture', 'Lecture'),
        ('Tutorial', 'Tutorial'),
        ('Lab', 'Lab'),
    )
    DAY_CHOICES = (
        ('MON', 'MON'),
        ('TUE', 'TUE'),
        ('WED', 'WED'),
        ('THU', 'THU'),
        ('FRI', 'FRI'),
        ('SAT', 'SAT'),
    )
    
    staff_email_id = models.CharField("Staff Email ID",  max_length=60, null = False)

    associated_program_code = models.CharField("Associated Program Code", max_length=255, null = True)

    academic_year_code = models.CharField("Academic Year Code", max_length=255, null = True)

    batch = models.CharField("Batch", max_length=255, null=True, blank=True)

    semester = models.CharField("Semester", max_length=255, unique=False)

    class_type = models.CharField("Class Type", max_length=255, choices=CLASS_TYPE_CHOICES)

    day = models.CharField("Day", max_length=255, choices=DAY_CHOICES)

    venue = models.CharField("Venue", max_length=255)

    start_time = models.CharField("Start Time", max_length=255)

    end_time = models.CharField("End Time", max_length=255)

    status = models.CharField("Status", max_length=255, choices=STATUS_CHOICES)



    def __str__(self):
        return self.staff_email_id
