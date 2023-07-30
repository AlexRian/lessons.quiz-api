from django.contrib import admin
from .models import Question, Answer

# Register your models here.
class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0
    fieldsets = (
        ('Answer', {
            'fields': ('text',),
        }),
    )

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]

