from django.db import models


# =========================
# DEPARTMENT
# =========================

class Department(models.Model):

    name = models.CharField(
        max_length=100
    )

    code = models.CharField(
        max_length=20,
        unique=True
    )

    def __str__(self):
        return f"{self.code} - {self.name}"


# =========================
# DEGREE OPTIONS
# =========================

DEGREE_CHOICES = [
    ('BE', 'B.E'),
    ('BTECH', 'B.Tech'),
    ('BSC', 'B.Sc'),
    ('BCA', 'BCA'),
    ('ME', 'M.E'),
    ('MTECH', 'M.Tech'),
    ('MSC', 'M.Sc'),
    ('MCA', 'MCA'),
    ('MBA', 'MBA'),
    ('PHD', 'Ph.D'),
]


# =========================
# STUDENT
# =========================

class Student(models.Model):

    student_id = models.CharField(
        max_length=20,
        unique=True
    )

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    dob = models.DateField(
        null=True,
        blank=True
    )

    gender = models.CharField(
        max_length=20,
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other'),
        ]
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=15
    )

    address = models.TextField()

    city = models.CharField(
        max_length=100
    )

    state = models.CharField(
        max_length=100
    )

    pincode = models.CharField(
        max_length=10
    )

    # Department dropdown
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    # Degree dropdown
    degree = models.CharField(
        max_length=20,
        choices=DEGREE_CHOICES,
        null=True,
        blank=True
    )

    admission_year = models.PositiveIntegerField()

    semester = models.PositiveIntegerField()

    section = models.CharField(
        max_length=10
    )

    enrollment_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=[
            ('Active', 'Active'),
            ('Inactive', 'Inactive'),
            ('Graduated', 'Graduated'),
        ],
        default='Active'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"