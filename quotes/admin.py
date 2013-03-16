from quotes.models import Quote
from django.contrib import admin

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('message', 'name', 'program', 'class_of',
                    'submission_time')

admin.site.register(Quote, QuoteAdmin)
