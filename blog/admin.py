from django.contrib import admin

from .models import blogpost
from django.db import models
from tinymce.widgets import TinyMCE

  
class textEditorAdmin(admin.ModelAdmin):
   list_display = ["title"]
   formfield_overrides = {
   models.TextField: {'widget': TinyMCE()}
   }


admin.site.register(blogpost, textEditorAdmin)
