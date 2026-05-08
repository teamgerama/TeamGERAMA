from django.contrib import admin
from .models import School, Department, Programme, Course, Material

# This allows you to upload materials directly inside the Course page
class MaterialInline(admin.TabularInline):
    model = Material
    extra = 3  # Provides 3 empty rows to upload multiple files at once
    fields = ('title', 'file')

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')
    list_filter = ('school',)

@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')
    list_filter = ('department__school', 'department')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'programme', 'level', 'semester')
    list_filter = ('level', 'semester', 'programme')
    search_fields = ('name', 'code')
    # This enables the multiple upload section inside Course
    inlines = [MaterialInline]

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    # Added 'get_course_name' for better clarity in the list view
    list_display = ('title', 'get_course_code', 'get_course_name', 'get_level', 'get_semester', 'uploaded_at')
    list_filter = ('course__level', 'course__semester', 'course__programme')
    search_fields = ('title', 'course__name', 'course__code')

    def get_course_code(self, obj):
        return obj.course.code if obj.course else "No Course"
    get_course_code.short_description = 'Code'

    def get_course_name(self, obj):
        return obj.course.name if obj.course else "No Course"
    get_course_name.short_description = 'Course Name'

    def get_level(self, obj):
        return obj.course.get_level_display() if obj.course else "N/A"
    get_level.short_description = 'Level'

    def get_semester(self, obj):
        return obj.course.get_semester_display() if obj.course else "N/A"
    get_semester.short_description = 'Semester'