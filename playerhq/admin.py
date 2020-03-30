from django.contrib import admin

from playerhq.models import Games,Reviews
    
class game(admin.ModelAdmin):
    list_display = ('GameName','GameCategory')
    
class review(admin.ModelAdmin):
    list_display = ('GameName','ReviewerName')

admin.site.register(Reviews,review)
admin.site.register(Games, game)