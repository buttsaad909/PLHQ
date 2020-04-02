from django.contrib import admin

from playerhq.models import Games,Reviews

# These models and their values are displayed on the playerhq admin page

class game(admin.ModelAdmin):
    list_display = ('GameName','GameCategory')
    
class review(admin.ModelAdmin):
    list_display = ('GameName','ReviewerName')

admin.site.register(Reviews,review)
admin.site.register(Games, game)
