from django.db import models

# REMOVED: from .models import ... (Never import a file into itself)

class School(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self): return self.name

class Department(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=255)
    def __str__(self): return f"{self.name} ({self.school.name})"

class Programme(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='programmes')
    name = models.CharField(max_length=255)
    def __str__(self): return self.name

class Course(models.Model):
    LEVEL_CHOICES = [
        ('100', 'Level 100'),
        ('200', 'Level 200'),
        ('300', 'Level 300'),
        ('400', 'Level 400'),
    ]
    SEMESTER_CHOICES = [
        ('1', 'Semester 1'),
        ('2', 'Semester 2'),
    ]

    programme = models.ForeignKey(Programme, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20)
    level = models.CharField(max_length=3, choices=LEVEL_CHOICES, default='100')
    semester = models.CharField(max_length=1, choices=SEMESTER_CHOICES, default='1')

    def __str__(self):
        return f"{self.code} - {self.name}"

# MOVED: Material is now back at the left margin (No longer inside Course)
class Material(models.Model):
    # Adding related_name='materials' makes it easier for the template to find the files
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='materials')
    title = models.CharField(max_length=200, blank=True)
    file = models.FileField(upload_to='study_materials/')

    def __str__(self):
        return self.title if self.title else f"Material for {self.course.name}"
