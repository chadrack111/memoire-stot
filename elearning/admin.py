from django.contrib import admin
from .models import CustomUser,Category, Course, Module, Lesson, Enrollment, Review

# Register your models here.
admin.site.register(CustomUser)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1

class ModuleInline(admin.StackedInline):
    model = Module
    extra = 1
    show_change_link = True

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'instructor', 'level', 'duration', 'rating', 'published']
    list_filter = ['level', 'published', 'category', 'created_at']
    search_fields = ['title', 'description', 'instructor__first_name', 'instructor__last_name']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order', 'duration']
    list_filter = ['course']
    ordering = ['course', 'order']
    inlines = [LessonInline]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'module', 'order', 'duration']
    list_filter = ['module__course']
    ordering = ['module', 'order']

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'enrolled_at', 'completed']
    list_filter = ['completed', 'enrolled_at']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']