from django.contrib import admin
from .models import Experience, Responsibility, Skillset, Skills, Recommendations

# Register your models here.

admin.site.register(Experience)
admin.site.register(Responsibility)
admin.site.register(Skillset)
admin.site.register(Skills)
admin.site.register(Recommendations)
