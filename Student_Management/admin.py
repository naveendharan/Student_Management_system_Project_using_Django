from django.contrib import admin
from .models import Department, Student


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    list_display = (
        'code',
        'name',
    )

    search_fields = (
        'code',
        'name',
    )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        'student_id',
        'first_name',
        'last_name',
        'email',
        'department',
        'degree',
        'semester',
        'status',
    )

    search_fields = (
        'student_id',
        'first_name',
        'last_name',
        'email',
    )

    list_filter = (
        'department',
        'degree',
        'semester',
        'status',
    )