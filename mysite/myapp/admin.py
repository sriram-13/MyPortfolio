from django.contrib import admin
from .models import ProfilePic, Experience, Responsibility, Skillset, Skills, Recommendations, Home, HomeImage, Paragraph, Contact, Awards

# Register your models here.

admin.site.register(Experience)
admin.site.register(Responsibility)
admin.site.register(Awards)
admin.site.register(Skillset)
admin.site.register(Skills)
admin.site.register(Recommendations)
admin.site.register(Home)
admin.site.register(HomeImage)
admin.site.register(Paragraph)
admin.site.register(Contact)
admin.site.register(ProfilePic)