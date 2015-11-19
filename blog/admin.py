from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField
from .models import Profile


class EntryAdmin(MarkdownModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}
    # Next line is a workaround for Python 2.x
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}
    
class ProfileAdmin(admin.ModelAdmin):
	class Meta:
		model = Profile

admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Tag)
admin.site.register(Profile, ProfileAdmin)


