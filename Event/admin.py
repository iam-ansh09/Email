from django.contrib import admin
from Event.models import Email, Question,Timings
# Register your models here.

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('name','roll','submittedOn')

    def time(self,object:Email):
        try:
            event = Timings.objects.all()[0]
        except:
            return 'No event Defined'
        if(object.submittedOn>event.end):
            return 'late'
        elif(object.submittedOn<event.start):
            return 'early'
        else:
            return 'On Time'
            
@admin.register(Timings)
class TimingAdmin(admin.ModelAdmin):
    list_display = ('start','end')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk','statement')


