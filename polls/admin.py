# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.


from polls.models import *

# admin.site.register(Question) # 告诉管理站点Question 对象要有一个管理界面

#
# class QuestionAdmin(admin.ModelAdmin):
#
#     fields = ["pub_date", "question_text"] #field 不加s？
#
# admin.site.register(Question, QuestionAdmin)

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#
#     ]

# admin.site.register(Question, QuestionAdmin)

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):

    # class ChoiceInline(admin.StackedInline): 显示所有关联的Choice 对象的字段占用大量的屏幕空间。
    # 为了解决这个问题，Django提供了一种以表格的形式显示内嵌的相关联对象的方法；
    # 你只需改变一下ChoiceInline 的声明：class ChoiceInline(admin.TabularInline):

    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline] # 

admin.site.register(Question, QuestionAdmin)

# admin.site.register(Choice)

