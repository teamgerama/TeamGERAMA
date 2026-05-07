from django.shortcuts import render, get_object_or_404
from .models import School, Department, Programme, Course, Material


def programme_detail(request, pk):
    programme = get_object_or_404(Programme, pk=pk)
    selected_level = request.GET.get('level')
    selected_semester = request.GET.get('semester')

    # Fetch courses based on the selections
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