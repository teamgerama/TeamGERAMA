from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import School, Department, Programme, Material, Course

# 1. The New Green Landing Page
def home(request):
    return render(request, 'academy/home.html')

# 2. The Resource Entry Point (The "Explore Resources" destination)
def school_list(request):
    schools = School.objects.all()
    query = request.GET.get('q')

    # Initialize search results structure
    search_results = {
        'departments': [],
        'programmes': [],
        'courses': [],
        'materials': []
    }

    if query:
        search_results['departments'] = Department.objects.filter(name__icontains=query)
        search_results['programmes'] = Programme.objects.filter(name__icontains=query)
        search_results['courses'] = Course.objects.filter(
            Q(name__icontains=query) | Q(code__icontains=query)
        )
        search_results['materials'] = Material.objects.filter(
            Q(title__icontains=query) | Q(course__name__icontains=query)
        )

    return render(request, 'academy/school_list.html', {
        'schools': schools,
        'query': query,
        'results': search_results,
    })

# 3. The Programme Detail View
def programme_detail(request, pk):
    programme = get_object_or_404(Programme, pk=pk)
    selected_level = request.GET.get('level')
    selected_semester = request.GET.get('semester')

    courses = Course.objects.filter(programme=programme)

    if selected_level:
        courses = courses.filter(level=selected_level)
    if selected_semester:
        courses = courses.filter(semester=selected_semester)

    return render(request, 'academy/programme_detail.html', {
        'programme': programme,
        'courses': courses,
        'selected_level': selected_level,
        'selected_semester': selected_semester,
    })