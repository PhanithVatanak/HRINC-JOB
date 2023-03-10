from rest_framework import serializers
from . import models

class jobFunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobFunction
        fields = ['id', 'job_title']


class jobListSerializer(serializers.ModelSerializer):


    jobList_image_banner = serializers.ImageField(max_length=None)
    jobList_image_logo = serializers.ImageField(max_length=None)

    jobList_jobFunction = jobFunctionSerializer(many=True)


    class Meta:
        model = models.JobList
        fields = (
            'id',
            'jobList_title',
            'jobList_companyName',
            'jobList_location',
            'jobList_hire',
            'jobList_type',
            'jobList_experience',
            'jobList_jobFunction',
            'jobList_industry',
            'jobList_preferredApplicant',
            'jobList_requiredLanguage',
            'jobList_deadline',
            'jobList_image_banner',
            'jobList_image_logo',
            'jobList_summary',
            'jobList_responsibility',
            'jobList_qualification',
            'jobList_qualification_Education',
            'jobList_qualification_Experiences',
            'jobList_qualification_other_requirements',
            'jobList_user_name',
            'jobList_user_title',
            'jobList_user_phoneNumber',
            'jobList_user_email',
            'jobList_user_address',
        )
