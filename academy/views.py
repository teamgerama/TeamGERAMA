from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import School, Department, Programme, Material, Course


def home(request):
    query = request.GET.get('q')
    schools = School.objects.all()

    # Initialize search results structure
    search_results = {
        'departments': [],
        'programmes': [],
        'courses': [],  # Added courses to results
        'materials': []
    }

    if query:
        # Search across your engineering hierarchy
        search_results['departments'] = Department.objects.filter(name__icontains=query)
        search_results['programmes'] = Programme.objects.filter(name__icontains=query)

        # New: Search by course name or course code (e.g., "CENG")
        search_results['courses'] = Course.objects.filter(
            Q(name__icontains=query) | Q(code__icontains=query)
        )

        # New: Search materials by title OR the name of the course they belong to
        search_results['materials'] = Material.objects.filter(
            Q(title__icontains=query) | Q(course__name__icontains=query)
        )

    return render(request, 'academy/home.html', {
        'schools': schools,
        'query': query,
        'results': search_results,
    })


def programme_detail(request, pk):
    programme = get_object_or_404(Programme, pk=pk)
    selected_level = request.GET.get('level')
    selected_semester = request.GET.get('semester')

    # Filter courses belonging to this programme
    courses = Course.objects.filter(programme=programme)

    # Apply Level and Semester filters from the frontend buttons
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