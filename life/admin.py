from django.contrib import admin
from life.models import *

# Register your models here.
admin.site.register(Group)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(User)