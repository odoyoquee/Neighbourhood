from django.contrib import admin
from .models import Profile, Post,Comments,Neighbourhood,Business

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Neighbourhood)
admin.site.register(Business)

