from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):

    # Group fields into sections
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date Information", {
            "fields": ["pub_date"],
            "classes": ["collapse"],
        }),
    ]

    # Show choices inline inside question
    inlines = [ChoiceInline]

    # Columns in change list page
    list_display = ["question_text", "pub_date", "was_published_recently"]

    # Filter sidebar
    list_filter = ["pub_date"]

    # Search bar
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
