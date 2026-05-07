from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import School, Department, Programme, Material, Course # Added Course here

def home(request):
    query = request.GET.get('q')
    schools = School.objects.all()

    search_results = {
        'departments': [],
        'programmes': [],
        'materials': []
    }

    if query:
        search_results['departments'] = Department.objects.filter(name__icontains=query)
        search_results['programmes'] = Programme.objects.filter(name__icontains=query)
        search_results['materials'] = Material.objects.filter(
            Q(title__icontains=query) | Q(programme__name__icontains=query)
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

    # Start with all courses in this programme
    courses = Course.objects.filter(programme=programme)

    # Filter courses by Level and Semester if they are selected
    if selected_level:
        courses = courses.filter(level=selected_level)
    if selected_semester:
        courses = courses.filter(semester=selected_semester)

    return render(request, 'academy/programme_detail.html', {
        'programme': programme,
        'courses': courses, # We pass 'courses' instead of just 'materials'
        'selected_level': selected_level,
        'selected_semester': selected_semester,
    })