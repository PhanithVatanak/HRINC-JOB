from django.shortcuts import render, redirect
from . import models
from .serializers import jobListSerializer, jobFunctionSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q
from . import forms



# Create your views here.

# JobFunction
def jobFunctionTitle(request):
    jobFunction_Titles = models.JobFunction.objects.all()
    job_Lists = models.JobList.objects.all()

    search_job = request.GET.get('search_job')
    if search_job != '' and search_job is not None:
        job_Lists = job_Lists.filter(jobList_title__icontains=search_job)


    context = { 'jobFunction_Titles' : jobFunction_Titles , 'job_Lists' : job_Lists}
    return render(request, 'jobsite/home.html', context)


# JobList
def jobList(request):
    job_Lists = models.JobList.objects.all()
    jobFunction_Titles = models.JobFunction.objects.all()

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    jobFunctions = models.JobFunction.objects.filter(
        Q(id__icontains = q))

    context = { 'job_Lists' : job_Lists , 'jobFunction_Titles' : jobFunction_Titles , 'jobFunctions' : jobFunctions }
    return render(request, 'jobsite/jobList.html', context)


def jobListDetail(request, pk):
    jobDetail = models.JobList.objects.get(id=pk)

    context = { 'jobDetail' : jobDetail }
    return render(request,'jobsite/jobListDetail.html', context)


def jobListDelete(request, pk):
    jobDetail = models.JobList.objects.get(id=pk)
    jobDetail.delete()
    return redirect('home')



# API

class JobFunctionViewSet(viewsets.ModelViewSet):
    queryset = models.JobFunction.objects.all()
    serializer_class = jobFunctionSerializer


class JobListViewSet(viewsets.ModelViewSet):
    queryset = models.JobList.objects.all()
    serializer_class = jobListSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def jobList_Detail_api(request, pk):
    job_Lists = models.JobList.objects.get(id=pk)
    serializer = jobListSerializer(job_Lists, many=False)

    if request.method == 'PUT':
        serializer = jobListSerializer(serializer, instance=job_Lists, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        job_Lists.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(serializer.data)


def jobListForm(request):
    form = forms.jobListForm()

    if request.method == 'POST':
        form = forms.jobListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inputForm-api')

    context = { 'form' : form }
    return render(request, 'jobsite/jobListForm.html', context)


