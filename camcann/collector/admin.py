from django.contrib import admin

from .models import *

admin.site.register(Data)
admin.site.register(Ads)
admin.site.register(Tag)
admin.site.register(Queue)


@admin.register(TagHistory)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('tag','timestamp','action')

@admin.register(AdTarget)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('ad','person')


