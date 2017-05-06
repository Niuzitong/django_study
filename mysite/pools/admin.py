# @Author: 牛子铜 <niuzitong>
# @Date:   2017-04-29T18:23:05+08:00
# @Email:  niuzitong@nonobank.com
# @Filename: admin.py
# @Last modified by:   niuzitong
# @Last modified time: 2017-05-01T03:03:46+08:00


from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None, {
            'fields': ['question_text']
        }),
        ('Date information', {
            'fields': ['pub_date'],
            'classes':['collapse']
        }),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
