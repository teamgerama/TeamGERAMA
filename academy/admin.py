from django.contrib import admin
from .models import School, Department, Programme, Course, Material

# --- INLINES ---
# These allow you to jump from School -> Dept -> Programme -> Course in one flow.

class DepartmentInline(admin.TabularInline):
    model = Department
    extra = 1
    show_change_link = True

class ProgrammeInline(admin.TabularInline):
    model = Programme
    extra = 1
    show_change_link = True

class CourseInline(admin.TabularInline):
    model = Course
    extra = 1
    fields = ('code', 'name', 'level', 'semester')
    show_change_link = True

class MaterialInline(admin.TabularInline):
    model = Material
    extra = 1

# --- MAIN ADMIN INTERFACE ---

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')
    list_filter = ('school',)
    search_fields = ('name',)


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'get_school')
    list_filter = ('department__school', 'department')
    search_fields = ('name',)


    def get_school(self, obj):
        return obj.department.school
    get_school.short_description = 'School'

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # Simplified list for a cleaner "attractive" look
    list_display = ('code', 'name', 'level', 'semester')
    list_editable = ('level', 'semester')
    list_filter = ('programme__department__school', 'programme', 'level', 'semester')
    search_fields = ('name', 'code')


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    # Removed Title and redundant Dept info for a minimal look
    list_display = ('course', 'get_level', 'file')
    list_filter = ('course__level', 'course__semester')

    def get_level(self, obj):
        return obj.course.level
    get_level.short_description = 'Level'