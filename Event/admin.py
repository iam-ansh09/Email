from django.contrib import admin
from Event.models import Email,Timings
# Register your models here.

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('name','roll','time')

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
class EmailAdmin(admin.ModelAdmin):
    list_display = ('start','end')