from django.contrib import admin
from .models import School, Department, Programme, Material


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    # Performance boost: fetches related data in one go
    list_select_related = ('programme__department__school', 'programme__department')

    list_display = ('get_course', 'get_school', 'get_department', 'programme', 'level', 'semester', 'uploaded_at')

    list_filter = (
        'programme__department__school',
        'programme__department',
        'level',
        'semester'
    )

    search_fields = ('title', 'programme__name')

    # Renames 'title' column to 'Course'
    def get_course(self, obj):
        return obj.title

    get_course.short_description = 'Course'
    get_course.admin_order_field = 'title'

    def get_school(self, obj):
        return obj.programme.department.school

    get_school.short_description = 'School'

    def get_department(self, obj):
        return obj.programme.department

    get_department.short_description = 'Department'


# Register other models
admin.site.register(School)
admin.site.register(Department)
admin.site.register(Programme)