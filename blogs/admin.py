from django.contrib import admin
from .models import Publication 
# Register your models here.
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'updated_date')
    search_fields = ('title', 'content', 'author__username')
list_filter = ('published_date', 'update_date' 'author')


admin.site.register(Publication, PublicationAdmin)
