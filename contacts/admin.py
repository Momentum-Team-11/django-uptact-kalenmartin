from django.contrib import admin
from .models import Contact, Note

admin.site.register(Contact, Note)