from django.shortcuts import render, get_object_or_404
from django.db.models import Q
# Import all your models here so the search logic can see them
from .models import School, Department, Programme, Material



def home(request):
    query = request.GET.get('q')
    schools = School.objects.all()

    # Initialize search results structure
    search_results = {
        'departments': [],
        'programmes': [],
        'materials': []
    }

    if query:
        # Search across different levels of your hierarchy
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

    materials = Material.objects.filter(programme=programme)

    if selected_level:
        materials = materials.filter(level=selected_level)
    if selected_semester:
        materials = materials.filter(semester=selected_semester)

    return render(request, 'academy/programme_detail.html', {
        'programme': programme,
        'materials': materials,
        'selected_level': selected_level,
        'selected_semester': selected_semester,
    })

