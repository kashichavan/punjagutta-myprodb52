from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *

@register(Dept)
class DeptAdmin(admin.ModelAdmin):
    list_display=['dname','dloc']


@register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['ename','eage','dept']


# Register your models here.
