from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import School, Department, Programme, Course, Material, Announcement

# STAGE 1: Home
def home(request):
    query = request.GET.get('q')
    if query:
        programmes = Programme.objects.filter(name__icontains=query)
        courses = Course.objects.filter(
            Q(name__icontains=query) | Q(code__icontains=query)
        )
        return render(request, 'academy/search_results.html', {
            'query': query,
            'programmes': programmes,
            'courses': courses
        })

    announcements = Announcement.objects.all()[:3]
    return render(request, 'academy/home.html', {'announcements': announcements})

# STAGE 2: School List
def school_list(request):
    schools = School.objects.all()
    return render(request, 'academy/school_list.html', {'schools': schools})

# STAGE 3: School Detail
def school_detail(request, school_id):
    school = get_object_or_404(School, id=school_id)
    departments = Department.objects.filter(school=school)
    return render(request, 'academy/school_detail.html', {
        'school': school,
        'departments': departments
    })

# STAGE 4: Department Detail
def dept_detail(request, dept_id):
    department = get_object_or_404(Department, id=dept_id)
    programmes = Programme.objects.filter(department=department)
    return render(request, 'academy/dept_detail.html', {
        'department': department,
        'programmes': programmes
    })

# STAGE 5: Programme Detail
def programme_detail(request, pk):
    programme = get_object_or_404(Programme, pk=pk)
    levels = ['100', '200', '300', '400']
    return render(request, 'academy/programme_detail.html', {
        'programme': programme,
        'levels': levels
    })

# STAGE 6: Level Detail
def level_detail(request, pk, level):
    programme = get_object_or_404(Programme, pk=pk)
    return render(request, 'academy/level_detail.html', {
        'programme': programme,
        'level': level
    })

# STAGE 7: Semester Detail
def semester_detail(request, pk, level, semester):
    programme = get_object_or_404(Programme, pk=pk)
    courses = Course.objects.filter(
        programme=programme,
        level=level,
        semester=semester
    )
    return render(request, 'academy/semester_detail.html', {
        'programme': programme,
        'level': level,
        'semester': semester,
        'courses': courses
    })