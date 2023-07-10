from django.contrib import admin
from .models import Guest,Movie,Book_ticket

admin.site.register(Guest)
admin.site.register(Book_ticket)
admin.site.register(Movie)