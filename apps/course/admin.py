from django.contrib import admin
from course.models import Course,CourseClass,CourseSort,Lesson,Teacher
# Register your models here.

class CourseClassAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']


class CourseSortAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','price','learn_time','click_num']
    list_filter = ['name','price','learn_time','click_num']
    search_fields = ['name','price','learn_time','click_num']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['name','lesson_course','time']
    list_filter = ['name','lesson_course']
    search_fields = ['name','lesson_course']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['teacher_name','teacher_des','teacher_course']
    list_filter = ['teacher_name','teacher_des','teacher_course']
    search_fields = ['teacher_name','teacher_des','teacher_course']


admin.site.register(CourseClass,CourseClassAdmin)
admin.site.register(CourseSort,CourseSortAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(Teacher,TeacherAdmin)

# 第二种方法：使用装饰器
# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ['name','price','learn_time','click_num','image','describe']
#     list_filter = ['name','price','learn_time','click_num']
#     search_fields = ['name','price','learn_time','click_num']
#
#     class Meta:
#         verbose_name = u'课程'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name