from django.contrib import admin
from .models import Course, Msg, Quiz ,User
# Register your models here.

admin.site.register(Msg)
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Quiz)
# admin.site.register(User)
