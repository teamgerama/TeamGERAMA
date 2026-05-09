from django.contrib import admin
from .models import School, Department, Programme, Course, Material


# --- INLINES (The "Under the Parent" sections) ---

class DepartmentInline(admin.TabularInline):
    model = Department
    extra = 1
    show_change_link = True  # Allows you to click a link to go straight to the Dept editor


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
    """
    This is your primary entry point.
    Adding a School allows you to add Departments immediately.
    """
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [DepartmentInline]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """
    Editing a Department allows you to add Programmes immediately.
    """
    list_display = ('name', 'school')
    list_filter = ('school',)
    search_fields = ('name',)
    inlines = [ProgrammeInline]


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    """
    Editing a Programme allows you to add Courses immediately.
    """
    list_display = ('name', 'department', 'get_school')
    list_filter = ('department__school', 'department')
    search_fields = ('name',)
    inlines = [CourseInline]

    def get_school(self, obj):
        return obj.department.school

    get_school.short_description = 'School'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    Editing a Course allows you to add PDF Materials immediately.
    """
    list_display = ('code', 'name', 'level', 'semester', 'programme')
    list_editable = ('level', 'semester')  # Quick edits from the list view
    list_filter = ('programme__department__school', 'programme', 'level', 'semester')
    search_fields = ('name', 'code')
    inlines = [MaterialInline]


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'get_level', 'file')
    list_filter = ('course__level', 'course__semester')

    def get_level(self, obj):
        return obj.course.level