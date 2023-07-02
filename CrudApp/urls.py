from django.contrib import admin
from django.urls import path
from EmpApp.views import branchApi, employeeApi


urlpatterns = [
    path('branch/', branchApi),
    path('branch/<int:id>/', branchApi),
    path('employee/', employeeApi),
    path('employee/<int:id>/', employeeApi),
    path('admin/', admin.site.urls),
]