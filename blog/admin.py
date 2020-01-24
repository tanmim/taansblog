from django.contrib import admin
from .models import Post
from .models import User
from .models import Title
from .models import meaow


admin.site.register(Post)
admin.site.register(User)
admin.site.register(Title)
admin.site.register(meaow)