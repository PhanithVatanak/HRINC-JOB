from django.contrib import admin
from django.urls import path, include
from jobsite import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.SimpleRouter()
router.register('job-list', views.JobListViewSet)
router.register('job-function', views.JobFunctionViewSet)


urlpatterns = [

    path('joblist-api/', include(router.urls)),
    path('joblist-api/detail/<str:pk>/', views.jobList_Detail_api, name="detail-api"),
    path('joblist-api/inputForm/', views.jobListForm, name="inputForm-api"),

    path('admin/', admin.site.urls),
    path('home/', views.jobFunctionTitle, name="home"),
    path('joblist/', views.jobList, name="joblist"),
    path('detail/<str:pk>/', views.jobListDetail, name="jobListDetail"),
    path('delete/<str:pk>/', views.jobListDelete, name="jobListDelete"),


]

urlpatterns += [ ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
