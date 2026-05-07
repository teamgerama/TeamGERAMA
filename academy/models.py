from django.db import models

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

class Material(models.Model):
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

    programme = models.ForeignKey(Programme, on_delete=models.CASCADE, related_name='materials')
    title = models.CharField(max_length=255)
    level = models.CharField(max_length=3, choices=LEVEL_CHOICES, default='100')
    semester = models.CharField(max_length=1, choices=SEMESTER_CHOICES, default='1')
    file = models.FileField(upload_to='study_materials/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.level}-Sem{self.semester}] {self.title}"