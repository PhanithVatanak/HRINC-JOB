from django.db import models

# Create your models here.

class JobFunction(models.Model):
    def __str__(self):
        return self.job_title

    job_title = models.CharField(max_length=200)


class JobList(models.Model):
    def __str__(self):
        return self.jobList_title


    jobList_title = models.CharField(max_length=200)
    jobList_companyName = models.CharField(max_length=200)
    jobList_location = models.CharField(max_length=200)


    # Job Overview
    jobList_hire = models.IntegerField()
    jobList_type = models.CharField(max_length=200)
    jobList_experience = models.CharField(max_length=200)

    jobList_jobFunction = models.ManyToManyField(JobFunction, related_name='jobList_jobFunction')

    jobList_industry = models.CharField(max_length=200)
    jobList_preferredApplicant = models.CharField(max_length=100)
    jobList_requiredLanguage = models.CharField(max_length=200)
    jobList_deadline = models.CharField(max_length=100)

    jobList_image_banner = models.ImageField(default='employer_profile_cover.jpg', max_length=200)
    jobList_image_logo = models.ImageField(default='hrinc_sq_logo.jpg', max_length=200)
    jobList_summary = models.TextField(max_length=300, null=True, blank=True)

    # Responsibilities and Duties
    jobList_responsibility = models.TextField(null=True, blank=True)


    # Qualifications and Skills
    jobList_qualification = models.TextField(null=True, blank=True)
    jobList_qualification_Education = models.TextField(null=True, blank=True)
    jobList_qualification_Experiences = models.TextField(null=True, blank=True)
    jobList_qualification_other_requirements = models.TextField(null=True, blank=True)


    # How to Apply
    jobList_user_name = models.CharField(max_length=200)
    jobList_user_title = models.CharField(max_length=200)
    jobList_user_phoneNumber = models.CharField(max_length=200, null=True, blank=True)
    jobList_user_email = models.CharField(max_length=200)
    jobList_user_address = models.CharField(max_length=200)


