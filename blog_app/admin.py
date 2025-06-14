from django.contrib import admin
from .models import Post, Rating, Contact, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Rating)
admin.site.register(Contact)
admin.site.register(Comment)
