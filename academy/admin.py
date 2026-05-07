from django.contrib import admin
from .models import School, Department, Programme, Course, Material


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
    # This shows the Course hierarchy in the admin list
    list_display = ('code', 'name', 'programme', 'level', 'semester')
    list_filter = ('level', 'semester', 'programme')
    search_fields = ('name', 'code')


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    # We changed these to reference the COURSE fields
    list_display = ('title', 'get_course_code', 'get_level', 'get_semester', 'uploaded_at')

    # Filtering materials by the course's attributes
    list_filter = ('course__level', 'course__semester', 'course__programme')

    # Helper methods to show course info in the Material list
    def get_course_code(self, obj):
        return obj.course.code

    get_course_code.short_description = 'Course Code'

    def get_level(self, obj):
        return obj.course.level

    get_level.short_description = 'Level'

    def get_semester(self, obj):
        return obj.course.semester

    get_semester.short_description = 'Semester'