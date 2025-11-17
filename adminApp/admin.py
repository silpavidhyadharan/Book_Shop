from django.contrib import admin
from adminApp.models import BookDb,CategoryDb

# Register your models here.
admin.site.register(BookDb)
admin.site.register(CategoryDb)