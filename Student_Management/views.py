from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout 
from .forms import StudentForm
from .models import Student


def student_form(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("student_list")

    else:

        form = StudentForm()

    return render(
        request,
        "student_form.html",
        {
            "form": form
        }
    )


def student_list(request):

    students = Student.objects.all().order_by("-created_at")

    return render(
        request,
        "student_list.html",
        {
            "students": students
        }
    )


def edit_student(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():

            form.save()

            return redirect("student_list")

    else:

        form = StudentForm(
            instance=student
        )

    return render(
        request,
        "student_form.html",
        {
            "form": form,
            "edit_mode": True,
            "student": student
        }
    )
def delete_student(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    if request.method == "POST":

        student.delete()

        return redirect("student_list")

    return render(
        request,
        "student_confirm_delete.html",
        {
            "student": student
        }
    )
    
def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("student_list")

        else:

            return render(
                request,
                "login.html",
                {
                    "error": "Invalid username or password"
                }
            )

    return render(
        request,
        "login.html"
    )