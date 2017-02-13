# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.


from polls.models import Question

# admin.site.register(Question) # 告诉管理站点Question 对象要有一个管理界面


class QuestionAdmin(admin.ModelAdmin):

    fields = ["pub_date","question_text"] #field 不加s？
    
# admin.site.register(Question, QuestionAdmin)

# class QuestionAdmin(admin.ModelAdmin):
    # fieldset = [
        # (None,               {'fields': ['question_text']}),
        # ('Date information', {'fields': ['pub_date'],'classes': ['collapse']}),
    # ]
    #fieldset不加s？
admin.site.register(Question, QuestionAdmin)