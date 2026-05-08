from django.contrib import admin
from .models import School, Department, Programme, Course, Material

# These allow you to add sub-items directly on the parent page
class DepartmentInline(admin.TabularInline):
    model = Department
    extra = 1

class ProgrammeInline(admin.TabularInline):
    model = Programme
    extra = 1

class CourseInline(admin.TabularInline):
    model = Course
    extra = 1

class MaterialInline(admin.TabularInline):
    model = Material
    extra = 1

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [DepartmentInline]

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')
    list_filter = ('school',)
    inlines = [ProgrammeInline]

@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')
    list_filter = ('department__school', 'department')
    inlines = [CourseInline]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'level', 'semester', 'programme')
    list_filter = ('level', 'semester', 'programme')
    search_fields = ('name', 'code')
    inlines = [MaterialInline]

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'file')
    search_fields = ('title',)