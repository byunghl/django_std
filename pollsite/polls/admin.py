from django.contrib import admin
from polls.models import Poll, Choice

#Possible parameter can be used with ChoiceInline class: admin.StackedInline, admin.TabularInline
class ChoiceInline(admin.TabularInline):
	model = Choice;
	extra = 3

class PollAdmin(admin.ModelAdmin):
	list_display = ('question', 'pub_date', 'was_published_recently')
	fieldsets = [
		(None, {'fields': ['question']}),
		('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
	]
	inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)