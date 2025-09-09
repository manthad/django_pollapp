from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Choice
import datetime
from django.utils import timezone
# class ChoiceInline(admin.StackedInline): this will show in one after other whihc is consuming so much space
class ChoiceInline(admin.TabularInline): # this will show in tabular form
    model = Choice
    extra = 3  

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    # list_display = ["question_text", "pub_date"] 
    list_display = ["question_text", "pub_date", "was_published_recently"] 
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    @admin.display( # Here there is not filter option so we are creating it
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self, obj):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= obj.pub_date <= now 
    
    # search_fields = ["question_text"] 

    inlines = [ChoiceInline]
  

        
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
