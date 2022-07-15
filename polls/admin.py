from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# admin.StackedInline - alternative style
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    # display specific columns in list view
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)