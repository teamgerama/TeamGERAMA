from django.contrib import admin
from .models import School, Department, Programme, Course, Material


# --- INLINES ---

class MaterialInline(admin.TabularInline):
    model = Material
    extra = 1  # Gives you one empty row to upload a new file directly from the Course page
    fields = ('title', 'file')


class CourseInline(admin.TabularInline):
    model = Course
    extra = 0
    fields = ('code', 'name', 'level', 'semester')
    show_change_link = True


class ProgrammeInline(admin.TabularInline):
    model = Programme
    extra = 0
    show_change_link = True


class DepartmentInline(admin.TabularInline):
    model = Department
    extra = 0
    show_change_link = True


# --- MAIN ADMIN INTERFACE ---

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

    def get_school(self, obj):
        return obj.department.school

    get_school.short_description = 'School'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # Highly informative layout
    list_display = ('code', 'name', 'programme', 'level', 'semester')
    list_filter = ('programme', 'level', 'semester')
    search_fields = ('code', 'name')

    # MAGIC HAPPENS HERE: Upload materials directly inside the Course edit page!
    inlines = [MaterialInline]


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    # Professional, minimal list showing exactly what you need
    list_display = ('title', 'course', 'get_level', 'get_semester', 'file_status')
    list_filter = ('course__programme', 'course__level', 'course__semester')
    search_fields = ('title', 'course__code', 'course__name')

    def get_level(self, obj):
        return obj.course.level

    get_level.short_description = 'Level'

    def get_semester(self, obj):
        return obj.course.semester

    get_semester.short_description = 'Semester'

    def file_status(self, obj):
        if obj.file:
            return "✅ Uploaded"
        return "❌ Missing"

    file_status.short_description = 'File'