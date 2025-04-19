from django.contrib import admin

from publication.models import Comment, Publication

# Register your models here.

admin.site.register(Publication)
admin.site.register(Comment)