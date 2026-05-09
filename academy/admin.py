from django.contrib import admin
from .models import School, Department, Programme, Course, Material

# --- INLINES ---
# These allow you to manage child objects directly from the parent's page.

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
    # We include level and semester here to match our new drill-down logic
    fields = ('code', 'name', 'level', 'semester')
    show_change_link = True

class MaterialInline(admin.TabularInline):
    model = Material
    extra = 1

# --- ADMIN CLASSES ---

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [DepartmentInline]

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')
    list_filter = ('school',)
    search_fields = ('name',)
    inlines = [ProgrammeInline]

@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'get_school')
    list_filter = ('department__school', 'department')
    search_fields = ('name',)
    inlines = [CourseInline]

    # Helper to show the School in the Programme list
    def get_school(self, obj):
        return obj.department.school
    get_school.short_description = 'School'

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # Added 'level' and 'semester' to list_display so you can see them at a glance
    list_display = ('code', 'name', 'level', 'semester', 'programme')
    # list_editable allows you to change Level/Semester without clicking into the course
    list_editable = ('level', 'semester')
    # Filters on the right sidebar to drill down exactly like the website does
    list_filter = ('programme__department__school', 'programme', 'level', 'semester')
    search_fields = ('name', 'code')
    inlines = [MaterialInline]

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'get_level', 'get_semester', 'file')
    search_fields = ('title', 'course__name', 'course__code')
    list_filter = ('course__programme', 'course__level')

    def get_level(self, obj):
        return obj.course.level
    get_level.short_description = 'Level'

    def get_semester(self, obj):
        return obj.course.semester
    get_semester.short_description = 'Sem'