from django.urls import path

from . import views


urlpatterns = [

    path(
    'login/',
    views.login_view,
    name='login'
),
    # Add Student
    path(
        '',
        views.student_form,
        name='student_form'
    ),

    # Student List
    path(
        'students/',
        views.student_list,
        name='student_list'
    ),

    # Edit Student
    path(
        'students/edit/<int:student_id>/',
        views.edit_student,
        name='edit_student'
    ),

    # Delete Student
    path(
        'students/delete/<int:student_id>/',
        views.delete_student,
        name='delete_student'
    ),

]