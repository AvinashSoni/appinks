from django.contrib import admin

from .models import Option, Solution, Hint, Question


class ChoiceInline(admin.StackedInline):
    model = Option
    extra = 4

class ChoiceInline2(admin.StackedInline):
    model = Solution
    extra = 1
class ChoiceInline1(admin.StackedInline):
    model = Hint
    extra = 1
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline, ChoiceInline1, ChoiceInline2]




admin.site.register(Question, QuestionAdmin)