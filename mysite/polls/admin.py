from django.contrib import admin
from polls.models import Question


admin.site.site_header = "Polls Admin"
admin.site.site_title = "The world's coolest Admin Panel"
admin.site.index_title = "Polls Site"

# Register your models here.
admin.site.register(Question)
