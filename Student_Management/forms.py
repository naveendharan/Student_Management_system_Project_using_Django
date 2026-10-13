from django import forms
from .models import Student, Department


class StudentForm(forms.ModelForm):

    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        empty_label="Select Department"
    )

    class Meta:
        model = Student

        fields = [
            'student_id',
            'first_name',
            'last_name',
            'dob',
            'gender',
            'email',
            'phone',
            'address',
            'city',
            'state',
            'pincode',
            'department',
            'degree',
            'admission_year',
            'semester',
            'section',
            'enrollment_date',
            'status',
        ]

        widgets = {
            'dob': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'enrollment_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'address': forms.Textarea(
                attrs={
                    'rows': 3
                }
            ),
        }