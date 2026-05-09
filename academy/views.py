from django.shortcuts import render, get_object_or_404
from .models import School, Department, Programme, Course, Material

# STAGE 1: Home
def home(request):
    return render(request, 'academy/home.html')

# STAGE 2: School List
def school_list(request):
    schools = School.objects.all()
    return render(request, 'academy/school_list.html', {'schools': schools})

# STAGE 3: School Detail (The missing attribute causing the error)
def school_detail(request, school_id):
    school = get_object_or_404(School, id=school_id)
    departments = Department.objects.filter(school=school)
    return render(request, 'academy/school_detail.html', {
        'school': school,
        'departments': departments
    })

# STAGE 4: Department Detail (Also required by your URLs)
def dept_detail(request, dept_id):
    department = get_object_or_404(Department, id=dept_id)
    programmes = Programme.objects.filter(department=department)
    return render(request, 'academy/dept_detail.html', {
        'department': department,
        'programmes': programmes
    })

def programme_detail(request, pk):
    programme = get_object_or_404(Programme, pk=pk)
    # Define the levels here and pass them to the template
    levels = ['100', '200', '300', '400']
    return render(request, 'academy/programme_detail.html', {
        'programme': programme,
        'levels': levels
    })

# STAGE 6: Level Detail (Semester Selection)
def level_detail(request, pk, level):
    programme = get_object_or_404(Programme, pk=pk)
    return render(request, 'academy/level_detail.html', {
        'programme': programme,
        'level': level
    })

# STAGE 7: Semester Detail (Course & Material List)
def semester_detail(request, pk, level, semester):
    programme = get_object_or_404(Programme, pk=pk)

    # This filter must match EXACTLY what is in the Admin
    courses = Course.objects.filter(
        programme=programme,
        level=level,
        semester=semester
    ).prefetch_related('material_set')  # This forces Django to grab the files early

    context = {
        'programme': programme,
        'level': level,
        'semester': semester,
        'courses': courses,
    }
    return render(request, 'academy/semester_detail.html', context)